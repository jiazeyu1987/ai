import numpy as np
import math
from .. import  *
class CircleEntity:
    def __init__(self):
        pass

    def caculate(self):
        pass

    def get_entity(self):
        q = [
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,
    0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,
    0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,
    0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,
    0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,
    0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            ]
        return np.asarray(q,np.int16).reshape(21,21)

def draw_circle(entity,item_value = 1):
    shape = entity.shape
    circle_center = ((int)((shape[0]-1)/2),(int)((shape[1]-1)/2))
    radius = math.floor(shape[0]*1/4)
    return draw_exact_circle(entity,circle_center,radius,item_value)

def draw_exact_circle(entity,center,radius,item_value):
    new_entity = create_clear_entity(entity)
    first_point = (center[0] + radius, center[1])
    box = [first_point]
    draw_point(new_entity, first_point, item_value)
    draw_circle_point_by_point(new_entity, center, radius, first_point, first_point, box,item_value)
    return (new_entity)

def draw_circle_point_by_point(entity,center_point,radius,father_point,elder,box,item_value):
    nearby = get_nearby_value(entity,father_point[0],father_point[1],-1)

    minV = 999
    minVal = None
    if(is_point_in_list(elder,nearby) and len(box)>3):
        return True

    for value in nearby:
        if(is_point_in_list(value,box)==False):
            radius_new = get_distance(value,center_point)
            distance = math.fabs(radius_new-radius)
            if(distance<minV):
                minV = distance
                minVal = value



    if(minVal!=None):
        newbox = box.copy()
        newbox.append(minVal)
        #time.sleep(1)
        draw_point(entity,minVal,item_value)
        draw_circle_point_by_point(entity,center_point,radius,minVal,elder,newbox,item_value)