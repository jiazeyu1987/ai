from .perception_base import *
from .perception_constant import *
class PerceptionTouching(PerceptionBase):
    def __init__(self,subtype):
        self.type = subtype
        PerceptionBase.__init__(self,TOUCHING)

    def __str__(self):
        return "perception touching:"+str(self.type)