import os
import os.path

from . settings import Config
from . baseobject import BaseObject

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

## add the objects to the factory
Config.objectFactory['plantbig'] = PlantBig
Config.objectFactory['plant'] = Plant        