import queue
from .attibute_perception import *
import  time
from person.action import *
class PerceptionMain:
    def __init__(self):
        self.perception_food = Food(self)
        self.perception_wanna_play = WannaPlay(self)
        self.queue = queue.Queue()
        pass


    def update(self):
        perceptionlist = self.get_all()
        return perceptionlist


    def on_watch_action(self,name1,action):
        print(action)
        if(action==ActionCry):
            perception_see = PerceptionSee(action,11)
            self.add_perception([perception_see])
        else:
            perception_see = PerceptionSee(action, 1)
            self.add_perception([perception_see])
        pass


    def add_perception(self,list1):
        self.queue.put(list1)


    def get_perception(self):
        if not self.queue .empty():
            return self.queue.get()


    def get_all(self):
        arr = []
        while not self.queue.empty():
            arr.append(self.queue.get())
        return arr
