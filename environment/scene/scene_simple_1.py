from person.perceptions import *
class SceneSimple1:
    def __init__(self):
        self.stim_arr = []
        self.init_stim_arr()

    def init_stim_arr(self):
        arr = [[create_perception(TOUCHING,100),create_perception(TOUCHING,101)],
               None,
               None,
               [create_perception(TOUCHING, 100), create_perception(TOUCHING, 101)],
               None,
               None,
               [create_perception(TOUCHING, 100), create_perception(TOUCHING, 101)],
               None,
               None,
               [create_perception(TOUCHING, 100), create_perception(TOUCHING, 101)],
               None,
               None,
               [create_perception(TOUCHING, 100), create_perception(TOUCHING, 101)],
               None,
               None,
               [create_perception(TOUCHING, 100), create_perception(TOUCHING, 101)],
               None,
               None,
               [create_perception(TOUCHING, 100), create_perception(TOUCHING, 101)],
               None,
               None,
               [create_perception(TOUCHING, 100), create_perception(TOUCHING, 101)],
               None,
               None,
               [create_perception(TOUCHING, 100), create_perception(TOUCHING, 101)],
               None,
               None,
               [create_perception(TOUCHING, 100), create_perception(TOUCHING, 101)],
               None,
               None
               ]
        self.stim_arr = arr

    def get_scene_piece(self):
        if(len(self.stim_arr)==0):
            return
        val = self.stim_arr[0]
        self.stim_arr = self.stim_arr[1:]
        return val

    def add_action(self,val):
        pass