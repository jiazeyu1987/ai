from . import *
from .. import *
class PerceptionSee(PerceptionBase):
    def __init__(self,val,degree):
        PerceptionBase.__init__(self, "see")
        self.degree = degree
        self.value =val

    @classmethod
    def unique_flag(cls):
        str1 = "perception:see"
        return str1

    @classmethod
    def unique_flag_with_value(cls,value):
        str1 = "perception:see&"+value.__str__()
        return str1