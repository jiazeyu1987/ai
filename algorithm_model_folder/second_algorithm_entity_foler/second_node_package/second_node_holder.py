from . import *
class SecondNodeObject(SecondNodeBase):
    def __init__(self,id):
        SecondNodeBase.__init__(self,id,"normal")

    def set_host(self,obj):
        self.host = obj

    def equal(self,*arg):
        if(len(arg)!=1):
            raise Exception("jjjj")
        node1 = arg[0]
        return self.host.id==node1.host.id



    def __str__(self):
        str1 = ""
        str1 = str1+self.id.__str__()
        str1 = str1+"("+self.host.name+")"
        return str1