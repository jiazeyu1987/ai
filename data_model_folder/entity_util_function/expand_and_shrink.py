import math
import time
import numpy as np
from .square_3_functions import  *
from ..entiti_utils import *
def expand(entity):
    current_point = _get_a_outter_point(entity)
    find_next_neighbour_point(entity,current_point,current_point,None,0,[1],2)
    find_next_neighbour_point(entity, current_point, current_point, None, 0,[1,2],3)
    change_value(entity, 3, 2)
    find_next_neighbour_point(entity, current_point, current_point, None, 0, [1, 2], 3)
    change_value(entity, 3, 2)

    inner_point = _get_a_inner_point(entity, [1,5])
    find_next_neighbour_point(entity, inner_point, inner_point, None, 0, [1], 5)
    inner_point = _get_a_inner_point(entity, [1,5])
    find_next_neighbour_point(entity, inner_point, inner_point, None, 0, [1, 5], 6)
    change_value(entity, 6, 5)
    inner_point = _get_a_inner_point(entity, [1,5])
    find_next_neighbour_point(entity, inner_point, inner_point, None, 0, [1, 5], 6)
    change_value(entity, 6, 5)

    inner_point = _get_a_inner_point(entity, [1,5])
    find_next_neighbour_point(entity, inner_point, inner_point, None, 0, [1, 5], 6)
    change_value(entity, 6, 5)
    print(entity)


def shrink(entity):
    inner_point = _get_a_inner_point(entity,[1])
    find_next_neighbour_point(entity,inner_point,inner_point,None,0,[1],2)
    inner_point = _get_a_inner_point(entity,[2])
    find_next_neighbour_point(entity, inner_point, inner_point, None, 0, [1,2], 3)
    inner_point = _get_a_inner_point(entity, [3])
    change_value(entity,3,2)
    find_next_neighbour_point(entity, inner_point, inner_point, None, 0, [1, 2], 3)
    inner_point = _get_a_inner_point(entity, [3])
    change_value(entity, 3, 2)
    find_next_neighbour_point(entity, inner_point, inner_point, None, 0, [1, 2], 3)
    inner_point = _get_a_inner_point(entity, [3])
    change_value(entity, 3, 2)
    find_next_neighbour_point(entity, inner_point, inner_point, None, 0, [1, 2], 3)
    inner_point = _get_a_inner_point(entity, [3])
    change_value(entity, 3, 2)
    #draw_point(entity,inner_point,5)
    print(entity)

def _get_a_inner_point(entity,vals):
    shape = entity.shape
    for i in range(shape[0]):
        valid_arr = []
        for j in range(shape[1]):
            if(is_point_has_value(entity,i,j,vals)):
                valid_arr.append(j)
        if(len(valid_arr)>1):
            for k in range(valid_arr[0],shape[1]):
                if(in_list(k,valid_arr)==False and k<valid_arr[len(valid_arr)-1]):
                    return (i,k)
            # if(is_point_has_value(entity,i,j,val)==False and
            #         is_point_has_value(entity,i,j+1,val)==True and
            #         is_point_has_value(entity,i,j+2,val)==False and
            #         (j+2)<entity.shape[1]):
            #     return (i,j+2)

def _get_a_outter_point(entity):
    shape = entity.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            if(entity[i][j]!=0):
                print(i,j,i,j-1)
                return (i,j-1)

def find_next_neighbour_point(entity,elder_point,current_point,father_point,depth,source_val,dest_val):
    if(elder_point==None):
        return
    draw_point(entity, current_point, dest_val)


    #time.sleep(1)
    #print(entity)
    if(is_near(elder_point,current_point) and depth>3):
        return
    new_depth = depth+1

    arr = get_3_square_value_arr(entity, current_point)




    return_point_number = None
    if(father_point!=None):
        if (in_point_position(entity,father_point,current_point,[0,2,6,8])):
            barr = []
            di = get_point_position(entity, father_point, current_point)
            if(di == 0):
                barr = [1,2,5,8,7,6,3]
            if(di == 2):
                barr = [5,8,7,6,3,0,1]
            if(di == 8):
                barr = [7,6,3,0,1,2,5]
            if(di == 6):
                barr = [3,0,1,2,5,8,7]
            if (_expand_confirm(arr,barr,source_val,[1,2,4,6])):
                return_point_number = barr[0]
            elif (_expand_confirm(arr, barr, source_val, [2, 4, 6])):
                return_point_number = barr[1]
            elif (_expand_confirm(arr,barr,source_val,[3,4,6])):
                return_point_number = barr[2]
            elif (_expand_confirm(arr,barr,source_val,[0,2,4,5])):
                return_point_number = barr[6]
            elif(_expand_confirm(arr,barr,source_val,[0,2,4])):
                return_point_number = barr[5]
            elif (_expand_confirm(arr, barr, source_val, [0, 2, 3])):
                return_point_number = barr[4]
            elif (_expand_confirm(arr,barr,source_val,[4,6])):
                return_point_number = barr[3]
            elif(_expand_confirm(arr,barr,source_val,[5,6])):
                return_point_number = barr[4]
            elif (_expand_confirm(arr, barr, source_val, [0, 2])):
                return_point_number = barr[3]
            elif (_expand_confirm(arr, barr, source_val, [0, 1])):
                return_point_number = barr[2]
            elif (_expand_confirm(arr,barr,source_val,[6])):
                return_point_number = barr[5]
            elif (_expand_confirm(arr, barr, source_val, [0])):
                return_point_number = barr[1]
            else:
                str1 = str(p0)+str(p1)+str(p1)+str(p3)+str(p4)+str(p5)+str(p6)+str(p7)+str(p8)+str(father_point)+str(current_point)
                raise Exception(str1)
            k = 1
        elif(in_point_position(entity,father_point,current_point,[1,3,5,7])):
            barr = []
            di = get_point_position(entity,father_point,current_point)
            if (di == 1):
                barr = [2, 5, 8, 7, 6, 3, 0]
            if (di == 3):
                barr = [0, 1, 2, 5, 8, 7, 6]
            if (di == 5):
                barr = [8, 7, 6, 3, 0, 1, 2]
            if (di == 7):
                barr = [6, 3, 0, 1, 2, 5, 8]
            if (_expand_confirm(arr, barr, source_val, [0, 1, 3, 5])):
                return_point_number = barr[6]
            elif (_expand_confirm(arr, barr, source_val, [0, 1, 3, 4])):
                return_point_number = barr[5]
            elif (_expand_confirm(arr, barr, source_val, [1, 3, 5, 6])):
                return_point_number = barr[0]
            elif (_expand_confirm(arr, barr, source_val, [2, 3, 5, 6])):
                return_point_number = barr[1]
            elif (_expand_confirm(arr, barr, source_val, [0, 1, 3])):
                return_point_number = barr[4]
            elif (_expand_confirm(arr, barr, source_val, [0, 1, 2])):
                return_point_number = barr[3]
            elif (_expand_confirm(arr, barr, source_val, [3, 5, 6])):
                return_point_number = barr[2]
            elif (_expand_confirm(arr, barr, source_val, [4, 5, 6])):
                return_point_number = barr[3]
            elif (_expand_confirm(arr, barr, source_val, [0, 1])):
                return_point_number = barr[2]
            elif (_expand_confirm(arr, barr, source_val, [5, 6])):
                return_point_number = barr[4]
            elif (_expand_confirm(arr, barr, source_val, [0])):
                return_point_number = barr[1]
            elif (_expand_confirm(arr, barr, source_val, [ 6])):
                return_point_number = barr[5]
            else:
                str1 = str(p0) + str(p1) + str(p1) + str(p3) + str(p4) + str(p5) + str(p6) + str(p7) + str(p8)+str(father_point)+str(current_point)
                raise Exception(str1)
    else:
        tan1 = create_9_circle_array()
        va,return_point_number = find_snake_tail(entity,tan1,current_point,source_val)
        if(va==False):
            return


        # barr = [0,1,2,5,8,7,6,3]
        # for i in range(len(barr)):
        #     if(in_list(arr[barr[i]],source_val)):
        #         if (arr[barr[i-1]] == 0):
        #             return_point_number = i-1
        #             break
        #         elif(arr[barr[i+1]] == 0):
        #             return_point_number = i + 1
        #             break
        #         else:
        #             break
    return_point = get_point_by_position(entity,current_point,return_point_number)

    find_next_neighbour_point(entity, elder_point, return_point,current_point, new_depth,source_val, dest_val)

def _expand_confirm(arr,barr,source_val,value_box):
    for i in value_box:
        if in_list(arr[barr[i]],source_val)==False:
            return False
    return True





def is_point_has_value(entity,i,j,vals):
    shape = entity.shape
    if(i<1 or i>shape[0]-1 or j<1 or j>shape[1]-1):
        return False

    if(in_list(entity[i][j],vals)):
        return True

    return False
