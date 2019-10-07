#!/usr/bin/env python3

#from psd_tools import PSDImage
#from psd_tools import constants

# psd = PSDImage.open('example.psd')
# psd.compose().save('example.png')

# for layer in psd:
#     print(layer)

import subprocess
import os
import os.path
from PIL import Image, ImageDraw
import tempfile
import shutil

class Assets:
    def __init__(self):
        self.basedir = '../assets/room_templates'

class NormalRoomAsset(Assets):
    def __init__(self):
        super().__init__()
        self.persp = os.path.join(self.basedir, "normal/persp.png")
        self.size = (320,200)
        self.control_pos = (0,158)

class RoomMaker:
    def __init__(self):
        self.convert = "/usr/local/bin/convert"

        self.layers = []
        self.bg_color = (255,255,255) # white
        self.bg_trans = (0,0,0,0) # transparent
        self.control_color = (0,0,0) # black

    def RunCmd(self, cmd, args):

        arglist = [cmd] + args

        print("%s" % " ".join(arglist))
        r = subprocess.run(arglist, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print(r.returncode)
        print(r.stdout)
        print("-"* 80)
        print(r.stderr)

    def CreateRoom(self, name, asset):
        self.layers = []
        self.layers.append( ('bg', Image.new('RGB', asset.size, color=self.bg_color) ) )
        self.layers.append( ('controls', self.CreateControl(asset) ) )

        self.BuildPSD(name)

    def CreateControl(self, asset):
        img = Image.new('RGBA', asset.size, color=self.bg_trans)
        draw = ImageDraw.Draw(img)
        draw.rectangle( [ asset.control_pos, asset.size ], fill=self.control_color )
        return(img)

    def BuildPSD(self,outname):
        layer_dict = {}
        
        # save objects 
        for lname, limg in self.layers:
            layer_dict[lname] = tempfile.NamedTemporaryFile()
            limg.save("%s.png" % layer_dict[lname].name, format="PNG" )

        for i in layer_dict.keys():
            if not os.path.exists( "%s.png" %  layer_dict[i].name ):
                print("can't find layer %s file %s" % (i, "%s.png" %  layer_dict[i].name))


        # create flatten
        flatten = tempfile.NamedTemporaryFile()
 

        files = list(map(lambda x: "%s.png" % x.name, list(layer_dict.values())))
        cmd_flatten = files + ["-verbose", "-flatten", "%s.png" % flatten.name] 

        #cmd_psd = "%s %s %s.psd" % ("%s.png" % flatten.name, files, outname)
        cmd_psd = ["%s.png" % flatten.name] + files + [ "%s.psd" % outname ]

        self.RunCmd(self.convert, cmd_flatten)
        self.RunCmd(self.convert, cmd_psd)
        shutil.copyfile("%s.png" % flatten.name,"salida.png")
        #self.RunCmd(self.convert, cmd_psd)

        # close files
        #for i in layer_dict.keys():
        #    layer_dict[i].close()


def demo():
    size = (320,200)
    bg_color = (255,255,255) 
    
    control_pos = (0,158)
    control_size = (320,200)
    control_color = (0,0,0)

    #img = Image.new('RGB', size, color=bg_color)
    #img.save('bg.png')

    img = Image.new('RGBA', size, color=bg_trans)
    draw = ImageDraw.Draw(img)
    draw.rectangle( [ control_pos, control_size ], fill=control_color )
    img.save('control.png')

    # tricky thing
    # 1 - create flatten in reverse order
    # 2 - merge all the three layers with the flatten image first.
    # - it works.
    # mephisto:python assman$ convert bg.png control.png  -flatten out.png
    # mephisto:python assman$ convert out.png bg.png control.png out.psd

if __name__ == "__main__":

    rm = RoomMaker()
    rm.CreateRoom('first', NormalRoomAsset())