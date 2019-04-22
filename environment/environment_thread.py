import time
import threading
from timeline import *
from .scene import *
class EnvironmentThread(threading.Thread):
    def __init__(self,list1):
        super(EnvironmentThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.val=list1

    def run(self):#定义每个线程要运行的函数
        while True:
            for k in self.val.person_list:
                k.update_from_outside()
                if(k.is_in_scene()==False):
                    k.InScene(SceneSimple1())
            wait_short()
