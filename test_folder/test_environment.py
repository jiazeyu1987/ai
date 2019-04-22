from environment import *
from timeline import *
from person import *
import  random
def test_environment():
    timeline = TimeLineMain()
    environment = EnvironmentMain(timeline)
    person = PersonMain(timeline,random.randint(1,100))
    environment.add_person(person)
    time.sleep(1000000)