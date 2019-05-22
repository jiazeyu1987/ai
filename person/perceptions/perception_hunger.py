from . import *
from .. import *
class PerceptionHunger(PerceptionBase):
    def __init__(self,degree):
        PerceptionBase.__init__(self, "hunger")
        self.degree = degree





    @classmethod
    def unique_flag(cls):
        str1 = "perception:hunger"
        return str1