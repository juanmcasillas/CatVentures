import subprocess
import os
import os.path
from PIL import Image, ImageDraw
import tempfile
import shutil

from . settings import Config


class RoomMaker:
    def __init__(self):

        self.layers = []

    def RunCmd(self, cmd, args):

        arglist = [cmd] + args

        # print("%s" % " ".join(arglist))
        r = subprocess.run(arglist, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # print(r.returncode)
        # print(r.stdout)
        # print("-"* 80)
        # print(r.stderr)

    def CreateRoom(self, name, asset):
        self.layers = []
        self.layers.append(("bg", Image.new("RGB", asset.size, color=Config.bg_color)))
       

        # add room Assets
        asset.LoadAssets(self.layers)

        # masks

        self.layers.append(("mask_walkable", self.CreateMaskWalkable(asset)))
        self.layers.append(("mask_hotspots", self.CreateMaskHotSpots(asset)))
        self.layers.append(("mask_regions", self.CreateMaskRegions(asset)))
        self.layers.append(("mask_behinds", self.CreateMaskBehinds(asset)))

        # control (verb gui holder)
        self.layers.append(("controls", self.CreateControl(asset)))

        # build the PSD file (to edit)
        self.BuildPSD(name)

     


    def CreateControl(self, asset):
        "creates the box for the verbs in the bottom of the screen"
        img = Image.new("RGBA", asset.size, color=Config.bg_trans)
        draw = ImageDraw.Draw(img)
        draw.rectangle([asset.control_pos, asset.size], fill=Config.control_color)
        return img

    def CreateMaskWalkable(self, asset):
        "creates the mask to allow chars move arround the screen"
        return Image.open(asset.walkable)

    def CreateMaskHotSpots(self, asset):
        "creates the mask for the hotspots (add a mask for each object"
        img = Image.new("RGBA", asset.size, color=Config.bg_trans)
        img = asset.LoadHotSpots(img)
        return img

    def CreateMaskRegions(self, asset):
        "creates regions"
        img = Image.new("RGBA", asset.size, color=Config.bg_trans)
        return img

    def CreateMaskBehinds(self, asset):
        "create walk behinds (for things put in front)"
        img = Image.new("RGBA", asset.size, color=Config.bg_trans)
        img = asset.LoadBehinds(img)
        return img

    def BuildPSD(self, outname):
        layer_dict = {}
        preview_dict = {}
        print("creating room %s" % outname)

        # create destination directory for this room

        outdir = Config.outputdir(outname)
        outpsd = "%s/%s.psd" % (outdir,outname)
        outpng = "%s/%s.png" % (outdir,outname)
        if not os.path.exists(outdir):
            os.makedirs(outdir)

        # save each layer in one file
        for lname, limg in self.layers:
            print(" -> creating layer %s" % lname)
            layer_dict[lname] = tempfile.NamedTemporaryFile()
            limg.save(layer_dict[lname].name, format="PNG")
            cmd_label = [
                layer_dict[lname].name,
                "-set",
                "label",
                "%s" % lname,
                layer_dict[lname].name,
            ]
            # for the preview. Get the files not masks
            if not lname.startswith("mask_"):
               preview_dict[lname] = layer_dict[lname]    

            self.RunCmd(Config.convert, cmd_label)

        # create flatten
        flatten = tempfile.NamedTemporaryFile()

        # join all together
        # tricky thing
        # 1 - create flatten in reverse order
        # 2 - merge all the three layers with the flatten image first.
        # - it works.
        # mephisto:python assman$ convert bg.png control.png  -flatten out.png
        # mephisto:python assman$ convert out.png bg.png control.png out.psd

        # first, generate only the preview.
           
        files = list(map(lambda x: x.name, list(preview_dict.values())))
        cmd_flatten = files + ["-flatten", flatten.name]
        self.RunCmd(Config.convert, cmd_flatten)
        # preview ####
        shutil.copy(flatten.name,outpng)

        # now, do the rest, with masks

        files = list(map(lambda x: x.name, list(layer_dict.values())))
        cmd_flatten = files + ["-flatten", flatten.name]
        cmd_psd = [flatten.name] + files + Config.psd_options + [outpsd]

        self.RunCmd(Config.convert, cmd_flatten)
        self.RunCmd(Config.convert, cmd_psd)

        print(" ** written PSD: %s" % outpsd)
        print(" ** Written PNG: %s" % outpng)

        # build the masks ####
        for lname,limg in self.layers:
            if lname.startswith("mask_"):
                img_indexed = limg.convert("RGB") # discard alpha
                img_indexed = img_indexed.convert("P", palette=Image.ADAPTIVE, colors=16)
                mask_name = "%s/%s_%s.png" % (outdir,outname,lname)
                img_indexed.save(mask_name)
                print(" -- written layer: %s" % mask_name)

        
        print("Done.")