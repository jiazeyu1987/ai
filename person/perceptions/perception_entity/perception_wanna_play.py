from . import *
from .. import *
class PerceptionWannaPlay(PerceptionBase):
    def __init__(self,degree):
        PerceptionBase.__init__(self, "wanna_play")
        self.degree = degree


    @classmethod
    def unique_flag(cls):
        str1 = "perception:wanna_play"
        return str1