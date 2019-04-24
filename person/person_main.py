import threading
import time

from person.perceptions import *
from person.decide_tree import *

class PersonMain:
    def __init__(self,timeline,name):
        self.name = name
        self.timeline = timeline
        self.current_scene = None
        self.perception = PerceptionMain()
        self.attribute = AttributeMain(self.perception)
        self.decide_tree = DecideTreeMain(self)
        self.action = ActionMain(self)
        t = threading.Thread(target=self.main_loop, args=())
        t.setDaemon(True)
        t.start()

    def main_loop(self):
        while self.attribute.die==False:
            self.update_from_inside()
            time.sleep(1)
        print("is died")


    def update_from_inside(self):
        #self.reflect_in_scene()
        self.attribute.update()
        perceptionlist = self.perception.update()
        self.decide_tree.update(perceptionlist)
        print("==================================")

    def update_from_outside(self):
        pass

    def InScene(self,scene):
        self.current_scene = scene

    def is_in_scene(self):
        return self.current_scene!=None



    def reflect_in_scene(self):
        if(self.current_scene is None):
            return
        scene_val = self.current_scene.get_scene_piece()
        self.perception.add_perception(scene_val)

        #action = self.current_scene.add_action(None)

