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
            mask = Image.alpha_composite(mask, src)

        return mask
