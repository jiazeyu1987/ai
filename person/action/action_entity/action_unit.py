from . import *
class ActionUnit(ActionBase):
    def __init__(self,key1):
        self.unit_key = key1
        ActionBase.__init__(self,"unit")

    @classmethod
    def unique_flag(cls):
        str1 = "action:unit"
        return str1

    @classmethod
    def create_key(cls,value):
        str1 = "action:unit&"+value
        return str1

    @classmethod
    def get_object(self,key):
        keylist = str.split(key,"&")
        val = keylist[1]
        obj = ActionUnit(val)
        return obj

