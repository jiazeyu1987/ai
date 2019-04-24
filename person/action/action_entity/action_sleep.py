from . import *
class ActionSleep(ActionBase):
    def __init__(self):
        ActionBase.__init__(self,"sleep")

    @classmethod
    def unique_flag(cls):
        str1 = "action:sleep"
        return str1