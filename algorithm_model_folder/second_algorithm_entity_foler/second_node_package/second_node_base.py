class SecondNode:
    def __init__(self,id):
        self.id = id
        self.host = None
        self.type = "obj"
        pass

    def set_host(self,obj):
        self.host = obj

    def print(self):
        print(self.id)





