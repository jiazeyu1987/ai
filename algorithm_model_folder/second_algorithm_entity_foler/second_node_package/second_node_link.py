from . import *
class SecondNodeHolder(SecondNodeBase):
    def __init__(self,id):
        SecondNodeBase.__init__(self,id,"holder")






    def __str__(self):
        str1 = ""
        str1 = str1+self.id.__str__()
        str1 = str1+"("+self.host.name+")"
        return str1