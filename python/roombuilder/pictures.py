import os
import os.path

from . settings import Config
from . baseobject import BaseObject

class PictureAlley(BaseObject):
    def __init__(self, coords, behind=False, hotspot=False):
        super().__init__(coords,behind,hotspot)
        self.res = {
            "img": os.path.join(self.basedir, "pictures/picture_alley.png"),
            "hotspot": os.path.join(self.basedir, "pictures/picture_alley_hotspot.png"),
        }
        self.name = "PictureAlley"

class PictureGuyBrush(BaseObject):
    def __init__(self, coords, behind=False, hotspot=False):
        super().__init__(coords,behind,hotspot)
        self.res = {
            "img": os.path.join(self.basedir, "pictures/picture_guybrush.png"),
            "hotspot": os.path.join(self.basedir, "pictures/picture_guybrush_hotspot.png"),
        }
        self.name = "PictureGuyBrush"

class PictureMM(BaseObject):
    def __init__(self, coords, behind=False, hotspot=False):
        super().__init__(coords,behind,hotspot)
        self.res = {
            "img": os.path.join(self.basedir, "pictures/picture_mm.png"),
            "hotspot": os.path.join(self.basedir, "pictures/picture_mm_hotspot.png"),
        }
        self.name = "PictureMM"


## add the objects to the factory
Config.objectFactory['picturealley'] = PictureAlley
Config.objectFactory['pictureguybrush'] = PictureGuyBrush        
Config.objectFactory['picturemm'] = PictureMM  