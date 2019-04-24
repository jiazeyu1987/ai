from . import *
class ActionPlay(ActionBase):
    def __init__(self):
        ActionBase.__init__(self,"play")

    @classmethod
    def unique_flag(cls):
        str1 = "action:play"
        return str1

    @classmethod
    def create(cls):
        str1 = ActionPlay.unique_flag()
        keylist = ["1-1","1-3","1-4","1-4","1-4","1-5","1-11","1-12","1-31"]
        strlist = [str1]
        for i in range(len(keylist)):
            key = ActionUnit.create_key(keylist[i])
            strlist.append(key)
        return strlist
