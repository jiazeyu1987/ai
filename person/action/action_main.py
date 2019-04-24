from .action_entity import *
class ActionMain:
    def __init__(self,person):
        self.person_main = person
        self.base_actions = self.init_tmp_base_action_collection()
        pass

    def do_action(self,str1):
        print("is doing action:",str1)

    def init_tmp_base_action_collection(self):
        arr = []
        for i in range(10):
            arr1 = []
            for j in range(100):
                key = str(i)+"-"+str(j)
                action_base = ActionUnit(key)
                arr1.append(action_base)
            arr.append(arr1)
        return arr