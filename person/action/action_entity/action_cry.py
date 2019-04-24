from . import *
class ActionCry(ActionBase):
    def __init__(self):
        ActionBase.__init__(self,"cry")

    @classmethod
    def unique_flag(cls):
        str1 = "action:cry"
        return str1

    @classmethod
    def create(cls):
        str1 = ActionCry.unique_flag()
        keylist = ["2-2", "2-3", "2-4", "2-4", "2-4", "2-5", "2-11", "2-12", "2-31"]
        strlist = [str1]
        for i in range(len(keylist)):
            key = ActionUnit.create_key(keylist[i])
            strlist.append(key)
        return strlist