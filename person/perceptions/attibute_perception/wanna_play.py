from ..perception_entity import *
class WannaPlay:
    def __init__(self,main):
        self.main = main
        pass
    
    def OnPlay(self,degree):
        if degree==1:
            pass
        elif degree==2:
            pass
        elif degree==3:
            pass
        elif degree==4:
            pass
        else:
            pass
        per = PerceptionWannaPlay(degree)
        self.main.add_perception([per])