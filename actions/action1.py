from person.perceptions import *
class Action1:
    def __init__(self):
        pass


    def run(self,timeline,perception_main):
        perception_main.add([timeline.get_ticker(),create_perception(TOUCHING),create_perception(TOUCHING)])
        wait_normal()
        perception_main.add([timeline.get_ticker(), create_perception(TOUCHING), create_perception(TOUCHING)])
        wait_normal()
        perception_main.add([timeline.get_ticker(), create_perception(TOUCHING), create_perception(TOUCHING)])
        wait_normal()
        perception_main.add([timeline.get_ticker(), create_perception(TOUCHING), create_perception(TOUCHING)])
        wait_normal()



        