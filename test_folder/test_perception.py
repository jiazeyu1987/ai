import time

from person.perceptions import *
from timeline import TimeLineMain


def test_perception():
    main = PerceptionMain()
    f = PerceptionTouching()
    timeline = TimeLineMain()
    time.sleep(2)
    tick = timeline.get_ticker()
    main.add([(f,tick)])
    pass