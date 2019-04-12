import math
import time
import numpy as np
from ..entiti_utils import *
import data_model_folder as dmf

def get_neighbor_of_val_0(entity,point):
    data_arr = [0,1,2,5,8,7,6,3]
    arr = []
    arr1 = get_all_neighbor_of_val_0(entity,point)
    if(dmf.expand_not_equal(entity,data_arr,point,[1,3],0)):
        arr1 = dmf.remove_point_from_list(arr1, dmf.get_point_by_position(point,data_arr[2]))
    if (dmf.expand_not_equal(entity,data_arr,point,[5,3],0)):
        arr1 = dmf.remove_point_from_list(arr1,dmf.get_point_by_position(point,data_arr[4]))
    if (dmf.expand_not_equal(entity,data_arr,point,[5,7],0)):
        arr1 = dmf.remove_point_from_list(arr1,dmf.get_point_by_position(point,data_arr[6]))
    if (dmf.expand_not_equal(entity,data_arr,point,[1,7],0)):
        arr1 = dmf.remove_point_from_list(arr1,dmf.get_point_by_position(point,data_arr[0]))
    return arr1


def get_all_neighbor_of_val_0(entity,point):

    arr = []
    for i in range(point[0]-1,point[0]+2):
        for j in range(point[1]-1,point[1]+2):
            if(i>-1 and j > -1 and i<entity.shape[0] and j < entity.shape[1]):
                if(entity[i][j]==0):
                    arr.append((i,j))
    return arr

def create_9_circle_array():
    big_arr = [0,1,2,5,8,7,6,3]
    arr = []
    for i in range(len(big_arr)):
        new_arr = []
        for j in range(len(big_arr)):
            new_arr.append(big_arr[(i+j)%len(big_arr)])
        arr.append(new_arr)
    #new_arr = [[0,1,2,5,8,7,6,3],[2,5,8,],[],[]]
    return arr

def find_snake_tail(entity,arr,source_point,source_val):
    for list1 in arr:
        if (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3],list1[5],list1[7]], source_val)):
            return False,None
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3],list1[5],list1[6]], source_val)):
            return True,list1[7]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[5],list1[3],list1[2]], source_val)):
            return True,list1[1]
        elif (in_all_position_is_value(entity, source_point, [list1[1],  list1[3],  list1[5],  list1[7]], source_val)):
            return False, None
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[5],list1[3]], source_val)):
            return True,list1[2]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3],list1[5]], source_val)):
            return True,list1[6]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[5],list1[4]], source_val)):
            return True,list1[3]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3],list1[4]], source_val)):
            return True,list1[5]
        elif (in_all_position_is_value(entity, source_point, [list1[1],  list1[3],  list1[5],  list1[6]], source_val)):
            return True, list1[7]
        elif (in_all_position_is_value(entity, source_point, [list1[1],  list1[4],  list1[5],  list1[7]], source_val)):
            return True, list1[3]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[3]], source_val)):
            return True,list1[4]
        elif (in_all_position_is_value(entity, source_point, [list1[1],  list1[3],  list1[5]], source_val)):
            return True, list1[6]
        elif (in_all_position_is_value(entity, source_point, [list1[1],  list1[5],  list1[7]], source_val)):
            return True, list1[4]
        elif (in_all_position_is_value(entity, source_point, [list1[1],  list1[3],  list1[4]], source_val)):
            return True, list1[5]
        elif (in_all_position_is_value(entity, source_point, [list1[1],  list1[7],  list1[6]], source_val)):
            return True, list1[5]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[5]], source_val)):
            return True,list1[5]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1],list1[2]], source_val)):
            return True,list1[3]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7],list1[6]], source_val)):
            return True,list1[5]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[1]], source_val)):
            return True,list1[2]
        elif (in_all_position_is_value(entity, source_point, [list1[1],  list1[3]], source_val)):
            return True, list1[4]
        elif (in_all_position_is_value(entity, source_point, [list1[1], list1[7]], source_val)):
            return True, list1[6]
        elif (in_all_position_is_value(entity, source_point, [list1[1], list1[2]], source_val)):
            return True, list1[3]
        elif (in_all_position_is_value(entity, source_point, [list1[0],list1[7]], source_val)):
            return True,list1[6]
        elif (in_all_position_is_value(entity, source_point, [list1[0]], source_val)):
            return True,list1[1]
    return False, None


def in_all_position_is_value(entity,source_point,arr,values):
    for i in arr:
        point1 = dmf.get_point_by_position(source_point,i)
        if(in_list(get_value_reverse(entity,point1),values)==False):
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