from person import *
from person.perceptions.perception_entity import *
class Food:
    def __init__(self,main):
        self.main = main
        pass
    
    def OnHunger(self,degree):
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
        per = PerceptionHunger(degree)
        self.main.add_perception([per])

    def OnFull(self,degree):
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
        per = PerceptionFull(degree)
        self.main.add_perception([per])