import os
import os.path
from PIL import Image, ImageDraw

from . settings import Config
from . baseassets import Assets

class Door(Assets):
    def __init__(self, pos, type, coords=None):
        super().__init__()
        self.doors = {
            "front": {
                "closed": os.path.join(self.basedir, "doors/door_front_closed.png"),
                "open": os.path.join(self.basedir, "doors/door_front_open.png"),
                "fullopen": os.path.join(self.basedir, "doors/door_front_fullopen.png"),
                "hotspot": os.path.join(self.basedir, "doors/door_front_hotspot.png"),
                # front is placed by coords
                #"xpos": 130,
                #"ypos": 12,
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
                "xpos": -44, # note the negative value
                "ypos": 20,
            },
            "bottom": {
                "closed": os.path.join(self.basedir, "doors/door_bottom_closed.png"),
                "open": os.path.join(self.basedir, "doors/door_bottom_open.png"),
                "fullopen": os.path.join(self.basedir, "doors/door_bottom_fullopen.png"),
                "hotspot": os.path.join(self.basedir, "doors/door_bottom_hotspot.png"),
                "behind": os.path.join(self.basedir, "doors/door_bottom_behind.png"),
                #"xpos": 150,
                #"ypos": 146,
            },
        }
        self.pos = pos.lower()
        self.type = type.lower()
        if coords:
            self.coords = coords
        self.res = self.doors[self.pos]

    def LoadAssets(self, layers, layer_size=None):
        super().LoadAssets(layers)

        img_file = self.res[self.type]
        xpos,ypos = self.GetCoords()
        # manage relative values from the right, and bottom
        if xpos < 0: xpos = layer_size[0]+xpos
        if ypos < 0: ypos = layer_size[1]+ypos
            


        name = "door_%s_%s" % (self.pos, self.type)

        door = Image.open(img_file)
        door.load()
        # create the layer
        img = Image.new("RGBA", layer_size, color=Config.bg_trans)
        img.paste(door, (xpos, ypos))
        layers.append((name.lower(), img))

    def LoadHotSpots(self, mask):

        src = Image.new("RGBA", mask.size, color=Config.bg_trans)
        img_file = self.doors[self.pos]["hotspot"]
        img = Image.open(img_file)
        xpos,ypos = self.GetCoords()
        if xpos < 0: xpos = mask.size[0]+xpos
        if ypos < 0: ypos = mask.size[1]+ypos

        src.paste(img, (xpos, ypos))
        mask = Image.alpha_composite(mask, src)
        return mask

    def LoadBehinds(self, mask):
        "doors only have bottom behinds"
        if "bottom" == self.pos:
            src = Image.new("RGBA", mask.size, color=Config.bg_trans)
            img_file = self.doors[self.pos]["behind"]
            img = Image.open(img_file)
            xpos,ypos = self.GetCoords()
            if xpos < 0: xpos = mask.size[0]+xpos   
            if ypos < 0: ypos = mask.size[1]+ypos            

            src.paste(img, (xpos, ypos))
            mask = Image.alpha_composite(mask, src)

        return mask

    def GetCoords(self):
        if "xpos" in self.res.keys():
            xpos = self.res["xpos"]
            ypos = self.res["ypos"]
            return (xpos,ypos)
        else:
            return self.coords