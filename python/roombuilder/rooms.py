import os
import os.path
from PIL import Image, ImageDraw

from . baseassets import Assets

class NormalRoom(Assets):
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

class LongRoom(NormalRoom):
    def __init__(self, name):
        super().__init__(name)
       
        self.persp = os.path.join(self.basedir, "room_templates/long/persp.png")
        self.walkable = os.path.join(self.basedir, "room_templates/long/walkable.png")
        self.size = (520, 200)
    