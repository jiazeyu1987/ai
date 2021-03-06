from jtree import *
from person import *
from . import *
from queue import  Queue
class DecideTreeMain:
    def __init__(self,person_main):
        self.person_main = person_main
        self.search_tree = JTreeMain()
        self.running_list = []
        self.current_chain = None
        if(person_main.age<3):
            init_base_search_tree_child(self)
        if (person_main.age > 20):
            init_base_search_tree_mother(self)
        pass


    def update(self,list_of_perception_list):
        self.update_running_list(list_of_perception_list)
        self.do_running_list()


    def do_running_list(self):
        # 初始化的时候是空的
        if(self.running_list==[]):
            return
        # 初始化的时候是空的，换链的时候是空的
        if(self.current_chain==None):
            self.current_chain = self.running_list[len(self.running_list)-1]

        # 暂时不考虑分叉，只取第一个
        action_node = self.current_chain.get_next()
        # 如果当前的链条走完了，移除链条
        if(action_node==None or self.is_action_node(action_node.value)==False):
            self.running_list = self.running_list[0:len(self.running_list)-1]
            self.current_chain=None
            self.do_running_list()
            return

        # 查看看是否存在对应动作的链条
        action_chain = self.search_tree.find(action_node.value)

        if(action_chain==None):
            is_unit_action_node = (action_node.value[7:11]=="unit")
            # 如果不存在链条看是否是动作单元
            if(is_unit_action_node):
                self.person_main.action.do_action(action_node.value)
            else:
                raise Exception("no action chain no unit action:",action_node.value)
        else:
            self.running_list.append(action_chain)
            self.current_chain = action_chain
            self.do_running_list()

    def update_running_list(self,list_of_perception_list):
        #初始化的时候是空的
        if(list_of_perception_list==None or len(list_of_perception_list)==0):
            return

        if(self.search_tree.is_empty()):
            return
        #初始化的时候是空的，加入第一条链条
        if(len(self.running_list)==0):
            priority_perception = self.get_priority_perception(list_of_perception_list)
            #print(priority_perception.unique_flag())
            chain = self.search_tree.find(priority_perception.unique_flag())

            chain.linked_perception = priority_perception
            self.running_list.append(chain)
        #已经运行起来了
        else:
            current_perception = self.running_list[0].linked_perception
            priority_perception = self.get_priority_perception(list_of_perception_list)
            old_degree = current_perception.degree
            #如果当前的优先级太大了，那么需要考虑换链
            if(priority_perception.degree>old_degree):
                #优先级大的跟当前的是同一个东西，那么更新优先级，估计以后还需要做点其他的
                if(priority_perception.equal(current_perception)):
                    current_perception.degree = priority_perception.degree
                #如果不是同一个东西，那么需要换链
                #换链需要更新链表，还要把当前的链条清空，当前的动作清空
                else:
                    self.running_list = []
                    chain = self.search_tree.find(priority_perception.unique_flag())
                    print(priority_perception.unique_flag())
                    chain.linked_perception = priority_perception
                    self.running_list.append(chain)
                    self.current_chain = None

        prinr(self.running_list[0],self.running_list[0].linked_perception)

    def is_action_node(self,node_str1):
        strlist = str.split(node_str1,":")
        if(strlist!=None and len(strlist)>0 and strlist[0]=="action"):
            return True
        return False

    def get_priority_perception(self,list_of_perception_list):
        max_priority = -1
        perception = None
        for perception_list in list_of_perception_list:
            for k in perception_list:
                if(k.degree>max_priority):
                    max_priority = k.degree
                    perception = k
        return perception



