import time
import threading
from timeline import *
from .scene import *


class EnvironmentMain:
    def __init__(self,timeline):
        self.person_list = []
        self.timeline = timeline
        t = threading.Thread(target=self.main_loop, args=())
        t.setDaemon(True)
        t.start()
        pass

    def main_loop(self):
        while True:
            for k in self.person_list:
                alive = k.is_alive()
                if(alive):
                    k.update_from_outside()
                    action_unit = k.get_action_unit()
                    if(action_unit!=None and len(action_unit)>0):
                        self.broadcast(k,action_unit)
                if(k.is_in_scene()==False):
                    k.InScene(SceneSimple1())
            wait_short()

    def broadcast(self,sender,action_unit):
        for k in self.person_list:
            k.action.receive_action(sender,action_unit)

    def add_person(self,person):
        self.person_list.append(person)




