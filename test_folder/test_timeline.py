from timeline import *
import time

def test_timeline():
    m = TimeLineMain()
    time.sleep(5)
    m.index = 1000
    time.sleep(5)
    m.end()
    time.sleep(10000)