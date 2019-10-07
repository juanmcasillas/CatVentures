#!/usr/bin/env python3

import subprocess
import os
import os.path
from PIL import Image, ImageDraw
import tempfile
import shutil


class Config:
    convert = "/usr/local/bin/convert"
    bg_color = (255, 255, 255)  # white
    bg_trans = (0, 0, 0, 0)  # transparent
    control_color = (0, 0, 0)  # black
    basedir = "../assets"
    default_screen_size = (320, 200)
    # right options to build a PSD file.

    psd_options = [
        "-depth",
        "8",
        "-type",
        "truecoloralpha",
        "-set",
        "colorspace:auto-grayscale",
        "off",
    ]


class Assets:
    def __init__(self):
        self.basedir = Config.basedir

    def LoadAssets(self, layers, layer_size=None):
        pass


class Door(Assets):
    def __init__(self, pos, type, coords=None):
        super().__init__()
        self.doors = {
            "front": {
                "closed": os.path.join(self.basedir, "doors/door_front_closed.png"),
                "open": os.path.join(self.basedir, "doors/door_front_open.png"),
                "fullopen": os.path.join(self.basedir, "doors/door_front_fullopen.png"),
                "hotspot": os.path.join(self.basedir, "doors/door_front_hotspot.png"),
                "xpos": 130,
                "ypos": 12,
            },
            "left": {
                "closed": os.path.join(self.basedir, "doors/door_left_closed.png"),
                "open": os.path.join(self.basedir, "doors/door_left_open.png"),
                "fullopen": os.path.join(self.basedir, "doors/door_left_fullopen.png"),
                "hotspot": os.path.join(self.basedir, "doors/door_left_hotspot.png"),
                "xpos": 7,
                "ypos": 20,
            },
            "right": {
                "closed": os.path.join(self.basedir, "doors/door_right_closed.png"),
                "open": os.path.join(self.basedir, "doors/door_right_open.png"),
                "fullopen": os.path.join(self.basedir, "doors/door_right_fullopen.png"),
                "hotspot": os.path.join(self.basedir, "doors/door_right_hotspot.png"),
                "xpos": 276,
                "ypos": 20,
            },
            "bottom": {
                "closed": os.path.join(self.basedir, "doors/door_bottom_closed.png"),
                "open": os.path.join(self.basedir, "doors/door_bottom_open.png"),
                "fullopen": os.path.join(self.basedir, "doors/door_bottom_fullopen.png"),
                "hotspot": os.path.join(self.basedir, "doors/door_bottom_hotspot.png"),
                "behind": os.path.join(self.basedir, "doors/door_bottom_behind.png"),
                "xpos": 150,
                "ypos": 146,
            },
        }
        self.pos = pos
        self.type = type
        self.coords = coords

    def LoadAssets(self, layers, layer_size=None):
        super().LoadAssets(layers)

        img_file = self.doors[self.pos.lower()][self.type.lower()]
        xpos = self.doors[self.pos.lower()]["xpos"]
        ypos = self.doors[self.pos.lower()]["ypos"]

        name = "door_%s_%s" % (self.pos, self.type)

        door = Image.open(img_file)
        door.load()
        # create the layer
        img = Image.new("RGBA", layer_size, color=Config.bg_trans)
        img.paste(door, (xpos, ypos))
        layers.append((name.lower(), img))

    def LoadHotSpots(self, mask):

        src = Image.new("RGBA", mask.size, color=Config.bg_trans)
        img_file = self.doors[self.pos.lower()]["hotspot"]
        img = Image.open(img_file)
        xpos = self.doors[self.pos.lower()]["xpos"]
        ypos = self.doors[self.pos.lower()]["ypos"]
        src.paste(img, (xpos, ypos))
        mask = Image.alpha_composite(mask, src)
        return mask

    def LoadBehinds(self, mask):
        "doors only have bottom behinds"
        if "bottom" == self.pos.lower():
            src = Image.new("RGBA", mask.size, color=Config.bg_trans)
            img_file = self.doors[self.pos.lower()]["behind"]
            img = Image.open(img_file)
            xpos = self.doors[self.pos.lower()]["xpos"]
            ypos = self.doors[self.pos.lower()]["ypos"]
            src.paste(img, (xpos, ypos))
            print(mask)
            mask = Image.alpha_composite(mask, src)

        return mask



class BaseObject(Assets):
    def __init__(self, coords, behind=False, hotspot=False):
        super().__init__()
        self.res = {
            "img": os.path.join(self.basedir, "furniture/XXXX.png"),
            "hotspot": os.path.join(self.basedir, "furniture/XXXX_hotspot.png"),
            "behind": os.path.join(self.basedir, "furniture/XXXX_behind.png"),
        }
        self.coords = coords
        self.name = "BaseObject"
        self.behind = behind
        self.hotspot = hotspot

    def LoadAssets(self, layers, layer_size=None):
        super().LoadAssets(layers)

        img_file = self.res["img"]
        xpos = self.coords[0]
        ypos = self.coords[1]

        name = "%s_%s_%s" % (self.name, xpos, ypos)

        img_file = Image.open(img_file)
        img_file.load()
        # create the layer
        img = Image.new("RGBA", layer_size, color=Config.bg_trans)
        img.paste(img_file, (xpos, ypos))
        layers.append((name.lower(), img))

    def LoadHotSpots(self, mask):

        if not self.hotspot:
            return mask

        src = Image.new("RGBA", mask.size, color=Config.bg_trans)
        img_file = self.res["hotspot"]
        img = Image.open(img_file)
        xpos = self.coords[0]
        ypos = self.coords[1]
        src.paste(img, (xpos, ypos))
        mask = Image.alpha_composite(mask, src)
        return mask

    def LoadBehinds(self, mask):

        if not self.behind:
            return mask

        src = Image.new("RGBA", mask.size, color=Config.bg_trans)
        img_file = self.res["behind"]
        img = Image.open(img_file)
        xpos = self.coords[0]
        ypos = self.coords[1]
        src.paste(img, (xpos, ypos))
        mask = Image.alpha_composite(mask, src)
        return mask
    



class PlantBig(BaseObject):
    def __init__(self, coords, behind=False, hotspot=False):
        super().__init__(coords,behind,hotspot)
        self.res = {
            "img": os.path.join(self.basedir, "furniture/plant_big.png"),
            "hotspot": os.path.join(self.basedir, "furniture/plant_big_hotspot.png"),
            "behind": os.path.join(self.basedir, "furniture/plant_big_behind.png"),
        }
        self.name = "plantBig"

class Plant(BaseObject):
    def __init__(self, coords, behind=False, hotspot=False):
        super().__init__(coords,behind,hotspot)
        self.res = {
            "img": os.path.join(self.basedir, "furniture/plant.png"),
            "hotspot": os.path.join(self.basedir, "furniture/plant_hotspot.png"),
            "behind": os.path.join(self.basedir, "furniture/plant_behind.png"),
        }
        self.name = "plant"
    
class RadiatorBig(BaseObject):
    def __init__(self, coords, behind=False, hotspot=False):
        super().__init__(coords,behind,hotspot)
        self.res = {
            "img": os.path.join(self.basedir, "furniture/radiator_big.png"),
            "hotspot": os.path.join(self.basedir, "furniture/radiator_big_hotspot.png"),
            "behind": os.path.join(self.basedir, "furniture/radiator_big_behind.png"),
        }
        self.name = "radiatorBig"

class Radiator(BaseObject):
    def __init__(self, coords, behind=False, hotspot=False):
        super().__init__(coords,behind,hotspot)
        self.res = {
            "img": os.path.join(self.basedir, "furniture/radiator.png"),
            "hotspot": os.path.join(self.basedir, "furniture/radiator_hotspot.png"),
            "behind": os.path.join(self.basedir, "furniture/radiator_behind.png"),
        }
        self.name = "radiator"

class NormalRoomAsset(Assets):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.persp = os.path.join(self.basedir, "room_templates/normal/persp.png")
        self.walkable = os.path.join(self.basedir, "room_templates/normal/walkable.png")
        self.size = (320, 200)
        self.control_pos = (0, 158)
        self.objects = []

    def AddObject(self, obj):
        self.objects.append(obj)

    def LoadAssets(self, layers):
        super().LoadAssets(layers)
        layers.append(("persp", Image.open(self.persp)))

        # add the objects
        for o in self.objects:
            o.LoadAssets(layers, layer_size=self.size)

    def LoadHotSpots(self, mask):
        for o in self.objects:
            mask = o.LoadHotSpots(mask)
        return mask

    def LoadBehinds(self, mask):
        for o in self.objects:
            mask = o.LoadBehinds(mask)
        return mask


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
        shutil.copy(flatten.name,"%s.png" % outname)

        # now, do the rest, with masks

        files = list(map(lambda x: x.name, list(layer_dict.values())))
        cmd_flatten = files + ["-flatten", flatten.name]
        cmd_psd = [flatten.name] + files + Config.psd_options + ["%s.psd" % outname]

        self.RunCmd(Config.convert, cmd_flatten)
        self.RunCmd(Config.convert, cmd_psd)

        print("Written %s.psd" % outname)
        print("Written %s.png" % outname)

if __name__ == "__main__":

    rm = RoomMaker()
    rm.CreateRoom("first_01", NormalRoomAsset("first"))

    room = NormalRoomAsset("second")
    room.AddObject(Door("Front", "FullOpen"))
    room.AddObject(Door("Left", "Open"))
    room.AddObject(Door("Right", "Closed"))
    room.AddObject(Door("Bottom", "Closed"))

    room.AddObject(PlantBig((20, 100), behind=True, hotspot=False))
    room.AddObject(Radiator((60, 85), behind=False, hotspot=True))


    # dummy objects
    room.AddObject(RadiatorBig((183, 85), behind=False, hotspot=False))
    room.AddObject(Plant((250, 90), behind=False, hotspot=False))


    rm.CreateRoom("second_02", room)
