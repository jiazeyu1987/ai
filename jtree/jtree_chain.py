from .jtree_node import JTreeNode
class JTreeChain:
    def __init__(self):
        self.chain_head = None
        self.linked_perception = None
        self.current_node = self.chain_head
        pass

    def get_next(self):
        if(self.current_node==None):
            self.current_node = self.chain_head
        next_nodes = self.current_node.next
        if(next_nodes!=None and len(next_nodes)>0):
            self.current_node = next_nodes[0]
        else:
            self.current_node = None
        return self.current_node

    def create_chain_by_strlist(self,strlist):
        jnodelist = []
        for i in range(len(strlist)):
            jnodelist.append(JTreeNode(strlist[i]))
        self.create_chain_by_jnodelist(jnodelist)

    def create_chain_by_jnodelist(self,jnodelist):
        if(len(jnodelist)==0):
            raise Exception("empty jnodelist in create chain")

        self.chain_head = jnodelist[0]

        start = self.chain_head
        for i in range(1,len(jnodelist)):
            start.add_next(jnodelist[i])
            start = jnodelist[i]


    # def get_node(self,number):
    #     start = self.chain_head
    #     for i in range(number):
    #         start
    #

    def __str__(self):
        return (self.chain_head.get_str())
