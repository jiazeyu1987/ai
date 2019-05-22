from . import *
class SecondNodeConnectorChangeLine(SecondNodeConnectorBase):

    def __init__(self,in_node,out_node,type1 = SecondNodeConnectorBase.Connect):
        SecondNodeConnectorBase.__init__(self)
        self.in_node = in_node
        self.out_node = out_node
        self.state = type1



