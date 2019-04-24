from . import *
from .. import *
class PerceptionFull(PerceptionBase):
    def __init__(self,degree):
        PerceptionBase.__init__(self, "full")
        self.degree = degree

    @classmethod
    def unique_flag(cls):
        str1 = "perception:full"
        return str1