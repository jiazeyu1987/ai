from . import *
class ActionWatching(ActionBase):
    def __init__(self):
        ActionBase.__init__(self,"watching")
        self.value = "watching"

    @classmethod
    def unique_flag(cls):
        str1 = "action:watching"
        return str1

    @classmethod
    def get_str_list(cls):
        keylist = ["5-3", "5-3", "5-4", "5-4"]
        return keylist

    @classmethod
    def create(cls):
        str1 = ActionWatching.unique_flag()
        keylist = ActionWatching.get_str_list()
        # newlist = []
        # for i in range(len(keylist)):
        #     newlist.append("action:unit&" + keylist[i])
        # keylist = newlist
        strlist = [str1]
        for i in range(len(keylist)):
            key = ActionUnit.create_key(keylist[i])
            strlist.append(key)
        return strlist

    @classmethod
    def find(cls, unitlist):
        keylist = ActionWatching.get_str_list()
        newlist = []
        for i in range(len(keylist)):
            newlist.append("action:unit&" + keylist[i])
        keylist = newlist
        len1 = len(keylist)
        len2 = len(unitlist)

        if (len2 > len1 - 1):
            sublist = unitlist[0:len1]
            if (sublist == keylist):
                return True, -2
            else:
                return False, -1
        else:
            for i in range(len2):
                if (keylist[i] != unitlist[i]):
                    return False, -1
            return True, keylist[len2]