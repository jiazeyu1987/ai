import time
import threading
from timeline import *
from .environment_thread import *

class EnvironmentEntity:
    def __init__(self):
        self.person_list = []
        pass

class EnvironmentMain:
    def __init__(self,timeline):
        self.val=EnvironmentEntity()
        self.timeline = timeline
        t = EnvironmentThread(self.val)
        t.setDaemon(True)
        t.start()
        pass

    def add_person(self,person):
        self.val.person_list.append(person)




