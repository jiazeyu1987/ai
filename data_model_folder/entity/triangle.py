import numpy as np
import math
import data_model_folder as dmf

class Triangle:
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
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,1,0,0,7,0,0,1,0,0,0,0,0,0,0,
    0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,
    0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
            ]
        return np.asarray(q,np.int16).reshape(20,20)
    
def draw_triangle(entity,top_point,len1,val,direction="down",is_solid=False):
    end_point1 = end_point2 = None
    if(direction=="up"):
        end_point1 = dmf.draw_oblique_line(entity, top_point, "up_right", len1, val)
        end_point2 = dmf.draw_oblique_line(entity, top_point, "up_left", len1, val)
    elif(direction=="right"):
        end_point1 = dmf.draw_oblique_line(entity, top_point, "up_right", len1, val)
        end_point2 = dmf.draw_oblique_line(entity, top_point, "down_right", len1, val)
    elif (direction == "down"):
        end_point1 = dmf.draw_oblique_line(entity, top_point, "down_left", len1, val)
        end_point2 = dmf.draw_oblique_line(entity, top_point, "down_right", len1, val)
    elif (direction == "left"):
        end_point1 = dmf.draw_oblique_line(entity, top_point, "down_left", len1, val)
        end_point2 = dmf.draw_oblique_line(entity, top_point, "up_left", len1, val)
    dmf.connect_two_point(entity,end_point2,end_point1,val)
    return entity