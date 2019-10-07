import os
import os.path

from . baseobject import BaseObject

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