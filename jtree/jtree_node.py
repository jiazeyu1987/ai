class JTreeNode:
    def __init__(self,val):
        self.value = val
        self.next = []
        self.pre = None

    def copy(self):
        jnode = JTreeNode()
        jnode.value = self.value
        return jnode

    def add_next(self,jnode):
        jnode.pre = self
        if(jnode in self.next):
            pass
        else:
            self.next.append(jnode)

    def has_next(self):
        return self.next!=[]

    def get_next(self):
        return self.next

    def set_parent(self,jnode):
        self.pre = jnode
        jnode.add_child(self)

    def add_child(self,jnode):
        if(self.has_child(jnode)):
            pass
        else:
            self.next.append(jnode)

    def has_child(self,jnode):
        for i in range(len(self.next)):
            if(self.next[i].equal(jnode)):
                return True
        return False

    def equal(self,jnode):
        return self.value ==jnode.value

    def get_str(self,head="   ",index=0):
        str1 = head*index
        str1 = str1+"value:" + self.value + "  child:"+str(len(self.next))+"\n"
        index+=1
        for i in range(len(self.next)):
            str1 = str1 + self.next[i].get_str(head,index)
        return str1

    def __str__(self):
        str1 = self.get_str()
        return str1
