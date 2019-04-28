from environment import *
from timeline import *
from person import *
import  random
def test_environment():
    timeline = TimeLineMain()
    environment = EnvironmentMain(timeline)
    person_child = PersonMain(timeline,random.randint(1,100),26)
    person_woman = PersonMain(timeline, random.randint(1, 100),1)
    environment.add_person(person_child)
    environment.add_person(person_woman)
    time.sleep(1000000)