import threading
import time
class TimeLineMain:
    def __init__(self):
        self.index = 0
        self.flag = True
        t = threading.Thread(target=self.start,args=())
        t.setDaemon(True)
        t.start()

        pass

    def start(self):
        while (self.flag):
            time.sleep(1)
            self.ticker()

    def ticker(self):
        self.index+=1


    def get_ticker(self):
        return self.index

    def reset(self):
        self.index = 1

    def end(self):
        self.flag = False