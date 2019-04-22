from person import  *
from person.perceptions import *
class PerceptionHunger(PerceptionBase):
    def __init__(self,degree):
        PerceptionBase.__init__(self, HUNGER,SOURCE_SELF)
        self.degree = degree