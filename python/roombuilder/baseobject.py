import os
import os.path
from PIL import Image, ImageDraw

from . settings import Config
from . baseassets import Assets

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

    def GetCoords(self):
        #xpos = self.coords[0]
        #ypos = self.coords[1]
        return self.coords

    def LoadAssets(self, layers, layer_size=None):
        super().LoadAssets(layers)

        img_file = self.res["img"]
        xpos,ypos = self.GetCoords()
        if xpos < 0: xpos = layer_size[0]+xpos
        if ypos < 0: ypos = layer_size[1]+ypos

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
        xpos,ypos = self.GetCoords()
        if xpos < 0: xpos = mask.size[0]+xpos
        if ypos < 0: ypos = mask.size[1]+ypos

        src.paste(img, (xpos, ypos))
        mask = Image.alpha_composite(mask, src)
        return mask

    def LoadBehinds(self, mask):

        if not self.behind:
            return mask

        src = Image.new("RGBA", mask.size, color=Config.bg_trans)
        img_file = self.res["behind"]
        img = Image.open(img_file)
        xpos,ypos = self.GetCoords()
        if xpos < 0: xpos = mask.size[0]+xpos
        if ypos < 0: ypos = mask.size[1]+ypos
        
        src.paste(img, (xpos, ypos))
        mask = Image.alpha_composite(mask, src)
        return mask
    
