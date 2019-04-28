from .action_entity import *
from person import *
class ActionMain:
    def __init__(self,person):
        self.person_main = person
        self.base_actions = self.init_tmp_base_action_collection()
        self.current_action_unit = []
        self.action_monitor = {}
        self.action_buildin = [ActionPlay,ActionSleep,ActionCry,ActionNurse,ActionWatching]
        pass


    def update(self):
        for name1 in self.action_monitor:
            actionlist = self.action_monitor[name1]
            action_class = self.combine_action_unit(name1,actionlist)
            if(action_class!=None):
                print(action_class.unique_flag())
                single_action = action_class
                self.action_monitor[name1]=[]
                if(name1!=self.person_main.name):
                    self.watched_action(name1,single_action)
                break


    def watched_action(self,name1,action):
        #print("JJJJJ:",name1,self.person_main.name,action.unique_flag())
        self.person_main.perception.on_watch_action(name1,action)
        pass

    def combine_action_unit(self,name,actionlist):
        dict1 = []
        for i in range(len(actionlist)):
            action_package = actionlist[i]
            action_sublist =action_package[0]
            time_index = action_package[1]
            for j in range(len(action_sublist)):
                action_unit = action_sublist[j]
                is_find = False
                for k in range(len(dict1)):
                    list_in_wait = dict1[k]
                    for action_class in self.action_buildin:
                        Flag,val = action_class.find(list_in_wait)
                        if(Flag):
                            if(val == action_unit):
                                is_find = True
                                dict1[k].append(action_unit)
                                break
                            if(val==-2):
                                return action_class
                        if(is_find):
                            break
                    if(is_find):
                        break
                if(is_find==False):
                    nd = [action_unit]
                    dict1.append(nd)
        return None


    def receive_action(self,sender,action_unit):
        if(sender.name in self.action_monitor):
            self.action_monitor[sender.name].append([action_unit,self.person_main.time_feeling_index])
        else:
            self.action_monitor[sender.name]=[[action_unit,self.person_main.time_feeling_index]]


    def do_action(self,str1):
        self.current_action_unit = [str1]
        prinr("is doing action:",str1)

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