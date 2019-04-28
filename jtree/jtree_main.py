from .jtree_chain import JTreeChain
from .jtree_node import JTreeNode
class JTreeMain:
    def __init__(self):
        self.dict = {}
        pass

    def is_empty(self):
        return len(self.dict)==0

    def find(self,string_key):
        if(string_key in self.dict):
            return self.dict[string_key]
        else:
            return None

    def add_chain(self,chain):
        self.add(chain.chain_head.value,chain)

    def add(self,string_key,chain):
        if(string_key in self.dict):
            old_chain = self.dict[string_key]
            new_chain = self.merge(old_chain,chain)
            self.dict[string_key] = new_chain
        else:
            self.dict[string_key] = chain

    def merge(self,old_chain,chain):
        self.merge_node(old_chain.chain_head,chain.chain_head)
        return (old_chain)

    def merge_node(self,old_node,node):
        flag_old = old_node.get_next()
        flag1 = node.get_next()
        if(flag_old!=None and flag1!=None):
            arr_differ,arr_same_old,arr_same_1 = self.jnodelist_minus(flag1, flag_old)
            for differ_node in arr_differ:
                differ_node.set_parent(old_node)
            for i in range(len(arr_same_1)):
                self.merge_node(arr_same_old[i],arr_same_1[i])


    def jnodelist_minus(self,list2,list_old):
        arr_differ = []
        arr_same_old =[]
        arr_same_2 = []
        for i in range(len(list2)):
            b = False
            same =None
            for j in range(len(list_old)):
                if(list_old[j].equal(list2[i])):
                    same = list_old[j]
                    b=True
                    break
            if(b==False):
                arr_differ.append(list2[i])
            else:
                arr_same_old.append(same)
                arr_same_2.append(list2[i])
        return arr_differ,arr_same_old,arr_same_2

    def jnodelist_equal(self,list1,list2):
        if(len(list1)!=len(list2)):
            return False

        for i in range(len(list1)):
            if(list1[i].equal(list2[i])==False):
                return False
        return True