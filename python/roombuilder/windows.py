import os
import os.path
from PIL import Image, ImageDraw

from . settings import Config
from . baseobject import BaseObject

class WindowBase(BaseObject):
    def __init__(self, coords, hotspot, bg=False):
        super().__init__(coords, False, hotspot)
        self.bg = bg

    def LoadAssets(self, layers, layer_size=None):
        
        # first, load the background or the white element; then, load the image using the super implementation.

        bg_res = "bgnone"
        if self.bg:
            bg_res = "bg"

        img_file = self.res[bg_res]
        xpos,ypos = self.GetCoords()

        name = "%s_%s_%s_%s" % (self.name, bg_res, xpos, ypos)

        img_file = Image.open(img_file)
        img_file.load()
        # create the layer
        img = Image.new("RGBA", layer_size, color=Config.bg_trans)
        img.paste(img_file, (xpos, ypos))
        layers.append((name.lower(), img))

        super().LoadAssets(layers, layer_size)
       

class WindowSmall(WindowBase):
    def __init__(self, coords, hotspot=False, bg=False):
        super().__init__(coords, hotspot, bg)
        self.windows = {
            "front": {
                "img": os.path.join(self.basedir, "windows/front_small/front_window_small.png"),
                "bg": os.path.join(self.basedir, "windows/front_small/front_window_small_bg.png"),
                "bgnone": os.path.join(self.basedir, "windows/front_small/front_window_small_bg_white.png"),
                "hotspot": os.path.join(self.basedir, "windows/front_small/front_window_small_hotspot.png"),
            }           
        }
        self.res = self.windows["front"]
        self.name = "windowSmall"

class Window(WindowBase):
    def __init__(self, pos, hotspot=False,bg=False, coords=None):
        super().__init__((0,0),hotspot, bg)
        self.windows = {
            "front": {
                "img": os.path.join(self.basedir, "windows/front/front_window.png"),
                "bg": os.path.join(self.basedir, "windows/front/front_window_bg.png"),
                "bgnone": os.path.join(self.basedir, "windows/front/front_window_bg_white.png"),
                "hotspot": os.path.join(self.basedir, "windows/front/front_window_hotspot.png")
                # front is placed by coords
                #"xpos": 7,
                #"ypos": 20,
            },            
            "left": {
                "img": os.path.join(self.basedir, "windows/left/left_window.png"),
                "bg": os.path.join(self.basedir, "windows/left/left_window_bg.png"),
                "bgnone": os.path.join(self.basedir, "windows/left/left_window_bg_white.png"),
                "hotspot": os.path.join(self.basedir, "windows/left/left_window_hotspot.png"),
                "xpos": 0,
                "ypos": 20,
            },
            "right": {
                "img": os.path.join(self.basedir, "windows/right/right_window.png"),
                "bg": os.path.join(self.basedir, "windows/right/right_window_bg.png"),
                "bgnone": os.path.join(self.basedir, "windows/right/right_window_bg_white.png"),
                "hotspot": os.path.join(self.basedir, "windows/right/right_window_hotspot.png"),
                "xpos": 276,
                "ypos": 20,                
            },
        }

        self.name = "window"
        self.bg = bg
        self.pos = pos.lower()
        if coords:
            self.coords = coords
        self.res = self.windows[self.pos]

    def GetCoords(self):
        if "xpos" in self.res.keys():
            xpos = self.res["xpos"]
            ypos = self.res["ypos"]
            return (xpos,ypos)
        else:
            return self.coords

