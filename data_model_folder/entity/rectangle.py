import numpy as np
import math
from .. import  *

class Rectangle:
    def __init__(self):
        pass

    def get_entity(self):
        q = [
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            ]
        return np.asarray(q,np.int16).reshape(20,20)
    
def draw_rectangle(entity,center_point,width,height,is_solid=False):
    shape = entity.shape
    row = shape[0]
    col = shape[1]

    if(is_point_position_legal(entity,center_point)==False):
        print(center_point)
        raise Exception("center point is illegal")

    if(width>row or height > col):
        print(row,col,width,height)
        raise Exception("width or height is out of range")

    if(center_point[0]+math.ceil(height/2)>col-1 or center_point[0]-math.ceil(height/2)<0):
        print(center_point,height,row,col)
        raise Exception("is out of range 1")

    if (center_point[1] + math.ceil(width / 2) > row - 1 or center_point[1] - math.ceil(width / 2) < 0):
        print(center_point, width, row, col)
        raise Exception("is out of range 2")

    left_half = math.floor(width/2)
    right_half = width - left_half
    up_half = math.floor(height/2)
    down_half = height - up_half

    left_up_point = (center_point[0]-up_half,center_point[1]-left_half)
    left_down_point = (center_point[0]+down_half-1,center_point[1]-left_half)
    right_up_point = (center_point[0]-up_half,center_point[1]+right_half-1)
    right_down_point = (center_point[0]+down_half-1,center_point[1]+right_half-1)

    if(is_solid==False):
        for i in range(left_up_point[1],right_up_point[1]+1):
            draw_point(entity,(left_up_point[0],i),1)
        for i in range(left_down_point[1],right_down_point[1]+1):
            draw_point(entity,(left_down_point[0],i),1)
        for i in range(left_up_point[0],left_down_point[0]+1):
            draw_point(entity,(i,left_up_point[1]),1)
        for i in range(right_up_point[0],right_down_point[0]+1):
            draw_point(entity,(i,right_up_point[1]),1)
    else:
        for i in range(left_up_point[1],right_up_point[1]+1):
            for j in range(right_up_point[0],right_down_point[0]+1):
                draw_point(entity, (j,i), 1)
    pass