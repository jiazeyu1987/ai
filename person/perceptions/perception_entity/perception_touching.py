from . import *
from .. import *
class PerceptionTouching(PerceptionBase):
    def __init__(self,subtype):
        self.type = subtype
        PerceptionBase.__init__(self,"touching")

    def __str__(self):
        return "perception touching:"+str(self.type)

    @classmethod
    def unique_flag(cls):
        str1 = "perception:touching"
        return str1