import math
import time
import numpy as np
from ..entiti_utils import *

def create_9_circle_array():
    big_arr = [0,1,2,5,8,7,6,3]
    arr = []
    for i in range(len(big_arr)):
        new_arr = []
        for j in range(len(big_arr)):
            new_arr.append(big_arr[(i+j)%len(big_arr)])
        arr.append(new_arr)
    return arr

def find_snake_tail(entity,arr,source_point,source_val):
    for list1 in arr:
        if (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3],list1[5],list1[7]], source_val)):
            return False,None
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3],list1[5],list1[6]], source_val)):
            return True,list1[7]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[5],list1[3],list1[2]], source_val)):
            return True,list1[1]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[5],list1[3]], source_val)):
            return True,list1[2]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3],list1[5]], source_val)):
            return True,list1[6]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[5],list1[4]], source_val)):
            return True,list1[3]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3],list1[4]], source_val)):
            return True,list1[5]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3]], source_val)):
            return True,list1[4]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[5]], source_val)):
            return True,list1[4]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[2]], source_val)):
            return True,list1[3]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[6]], source_val)):
            return True,list1[5]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1]], source_val)):
            return True,list1[2]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7]], source_val)):
            return True,list1[6]
        elif (in_all_position_is_value(entity, source_point, [list1[0]], source_val)):
            return True,list1[1]
    return False, None


def in_all_position_is_value(entity,source_point,arr,values):
    for i in arr:
        point1 = get_point_by_position(entity,source_point,i)
        if(in_list(get_value(entity,point1),values)==False):
            return False
    return True

def find_snake_tail2(arr,source_val,num):
    for i in range(len(arr)):
        isok = True
        for j in range(num):
            if(arr[i][j]!=num):
                isok = False
                break
        if(isok):
            return True,arr[i][num]
    return False,None