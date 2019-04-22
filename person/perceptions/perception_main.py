import queue
from .attibute_perception import *
import  time
class PerceptionMain:
    def __init__(self):
        self.perception_food = Food(self)
        self.queue = queue.Queue()
        pass


    def update(self):
        perceptionlist = self.get_all()
        print("is thinking")
        for k in perceptionlist:
            print(k)

    def add_perception(self,list1):
        self.queue.put(list1)


    def get_perception(self):
        if not self.queue .empty():
            return self.queue.get()


    def get_all(self):
        arr = []
        while not self.queue .empty():
            arr.append(self.queue.get())
        return arr
