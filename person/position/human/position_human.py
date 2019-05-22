from person.position import  *
from .. import PositionMain
class PositionHuman:
    def __init__(self):
        self.position_array = {}
        self.picture = []
        self.row = 9
        self.col = 9
        self.tag = "human"

    def create(self):
        a1 = PositionMain.CN()
        a2 = PositionMain.CN()
        a3 = PositionMain.CN()
        a4 = PositionMain.CN()
        a5 = PositionMain.CN()
        a6 = PositionMain.CN()
        a7 = PositionMain.CN()
        _picture = [
            0, 0,  0,  0,  a1, 0,  0,  0,  0,
            0, 0,  0,  0,  a6, 0,  0,  0,  0,
            0, a5, a4, a2, a2, a2, a4, a5, 0,
            0, 0,  0,  a2, a2, a2, 0,  0,  0,
            0, 0,  0,  a2, a2, a2, 0,  0,  0,
            0, 0,  0,  a3, a7, a3, 0,  0,  0,
            0, 0,  0,  a3, 0,  a3, 0,  0,  0,
            0, 0,  0,  6,  0,  6,  0,  0,  0,
            0, 0,  0,  0,  0,  0,  0,  0,  0,
        ]
        self.position_array[a1] = PositionHead()
        self.picture.append(np.asarray(_picture, np.int16).reshape(self.row, self.col))



