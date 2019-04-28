import threading
import time

from person.perceptions import *
from person.decide_tree import *


class PersonMain:
    def __init__(self,timeline,name,age):
        self.name = name
        self.age = age
        self.timeline = timeline
        self.current_scene = None
        self.perception = PerceptionMain()
        self.attribute = AttributeMain(self.perception)
        self.decide_tree = DecideTreeMain(self)
        self.action = ActionMain(self)
        self.current_time_unit = 0
        self.time_feeling_index = 0
        # t = threading.Thread(target=self.update_from_inside, args=())
        # t.setDaemon(True)
        # t.start()

    def is_alive(self):
        return self.attribute.die == False

    def update_from_inside(self):
        #self.reflect_in_scene()
        self.time_feeling_index+=1
        self.attribute.update()
        perceptionlist = self.perception.update()
        self.decide_tree.update(perceptionlist)
        self.action.update()
        time.sleep(1)
        prinr("==================================")



    def update_from_outside(self):
       if(self.is_alive()):
            self.current_time_unit+=1
            if(self.current_time_unit==react_time_unit):
                self.update_from_inside()
                self.current_time_unit=0

    def get_action_unit(self):
        unit = self.action.current_action_unit
        self.action.current_action_unit = None
        return unit

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

