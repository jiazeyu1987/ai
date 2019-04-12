class FirstAlgorithmChainNode:
    def __init__(self,type):
        self._type = type
        self._value = []
        self._next = None
        self._pre = None
        self._linked_nodes = []
        pass

    def to_string(self):
        str1 = self._type
        str1 = str1+":"+str(self._value)
        return str1

    def __str__(self):
        str2 = ""
        for k in self._linked_nodes:
            str1 = ""
            for j in k:
                str1 = str1+" "+str(j)+" "
            str2 = str2+"|"+str1+"|"
        if(len(str2)>0):
            return "chain node:"+"   type:"+self._type+"   value:"+str(self._value)+"       nodes:<<"+str2+">>"
        else:
            return "chain node:" + "   type:" + self._type + "   value:" + str(self._value)

    def get_type(self):
        return self._type

    def get_value(self):
        return self._value

    def add_nodes(self,values):
        if(len(values)==0):
            return
        self._linked_nodes.append(values)

    def add_value(self,value):
        self._value.append(value)

    def set_next(self,node):
        self._next = node
        node._pre = self

    def nodes_number(self):
        return len(self._linked_nodes)

    def find_all_pre_nodes(self,i):
        fnode = self.find_first_node()
        arr = []
        index = 0

        while(fnode.equal(self)==False):
            if(index<i):
                pass
            else:
                arr.append(fnode)
            index+=1
            fnode = fnode.next()
        # print("\n\n\n")
        # print("**********************")
        # print(self)
        # self.print_chain()
        # print(fnode)
        # print("**********************")
        return arr

    def set_clone(self,type,value,nodes):
        self._type = type
        self._value = value
        self._linked_nodes = nodes

    def clone(self):
        node = FirstAlgorithmChainNode("")
        node.set_clone(self._type,self._value,self._linked_nodes)
        return node

    def next(self):
        return  self._next

    def equal(self,chain_node):
        value1 = self._value
        value2 = chain_node._value
        if(value1==value2):
            return True
        else:
            return False

    def print_chain(self,type1=0):
        if(type1==0):
            print("chain start")
            first_node = self.find_first_node()
            while(first_node!=None):
                print(first_node)
                first_node = first_node._next
            print("chain end")
        else:
            first_node = self.find_first_node()
            str1 = "chain_node:"
            while (first_node != None):
                str1 = str1+first_node.to_string()
                str1 = str1+" "
                first_node = first_node._next
            print(str1)
            return str1



    def find_first_node(self):
        fnode = self
        while(fnode._pre!=None):
            fnode = fnode._pre
            #print(fnode)
        return fnode