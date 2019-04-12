import numpy as np
import math
import time
import data_model_folder as dmf

def in_list(v,list):
    for i in list:
        if(i==v):
            return True
    return False

def change_value(entity,from_value,to_value):
    for i in range(entity.shape[0]):
        for j in range(entity.shape[1]):
            if(entity[i][j]==from_value):
                entity[i][j] = to_value

def get_3_square_value_arr(entity,current_point):
    p0 = (entity[current_point[0] - 1, current_point[1] - 1])
    p1 = (entity[current_point[0] - 1, current_point[1]])
    p2 = (entity[current_point[0] - 1, current_point[1] + 1])
    p3 = (entity[current_point[0], current_point[1] - 1])
    p4 = (entity[current_point[0], current_point[1]])
    p5 = (entity[current_point[0], current_point[1] + 1])
    p6 = (entity[current_point[0] + 1, current_point[1] - 1])
    p7 = (entity[current_point[0] + 1, current_point[1]])
    p8 = (entity[current_point[0] + 1, current_point[1] + 1])
    arr = [p0, p1, p2, p3, p4, p5, p6, p7, p8]
    return arr



def is_near(p1,p2):
    return math.fabs(p1[0]-p2[0])<2 and math.fabs(p1[1]-p2[1])<2





def get_value_reverse(entity,point):
    return entity[point[0]][point[1]]


def generate_map(point_list):
    rowmap = {}
    colmap = {}
    for k in point_list:
        row = k[0]
        col = k[1]
        if(rowmap.__contains__(row)==False):
            rowmap[row] = []
            rowmap[row].append(k)
        if(colmap.__contains__(col)==False):
            colmap[col] = []
            colmap[col].append(k)
    return rowmap,colmap









def get_distance(point1,point2):
    return math.sqrt((point2[1]-point1[1])*(point2[1]-point1[1])+(point2[0]-point1[0])*(point2[0]-point1[0]))

# def draw_point(entity,point1,val):
#     entity[point1[0],point1[1]]=val

def create_clear_entity(entity):
    shape = entity.shape
    new = np.zeros(shape,np.int16)
    return new

def is_circle(entity):
    index = 0;
    shape = entity.get_entity().shape
    row = shape[0]
    col = shape[1]
    for i in range(row):
        for j in range(col):
            index+=1
    return index


def is_closed(data_model):
    # shape = data_model.shape
    # row = shape[0]
    # col = shape[1]
    # for i in range(row):
    #     for j in range(col):
    #         if(data_model[i][j]!=0):
    #             if(is_closed_item(data_model,i,j)):
    #                 pass
    # return False
    f,_ = dmf.is_has_a_hole(entity)
    if(f):
        return True
    else:
        return False

def is_closed_item(data_model,row,col):
    nearby = get_nearby_value(data_model,row,col,1)
    box = [(row,col)]
    v = _closed_alg_claw(data_model, (row, col), (row, col), box)
    if (len(v) > 0):
        return True
    else:
        return False

def _closed_alg_claw(data_model,des_val,val,box):
    nearby = get_nearby_value(data_model,val[0],val[1],1)
    arr = []
    for t_val in nearby:
        if(is_point_in_list(t_val,box)==False):
            if(t_val[0]==des_val[0] and t_val[1]==des_val[1]):
                pass
            else:
                newbox = box.copy()
                newbox.append(t_val)

                tal = _closed_alg_claw(data_model,des_val,t_val,newbox)
                if(len(tal)>0):
                    arr = arr+tal
        else:
            if(t_val==des_val and len(box)>2):
                #newbox = box.copy()
                #newbox.append(t_val)
                arr.append(box)
            pass
    return arr

def is_point_in_list(val,box):
    for key in box:
        if(key[0]==val[0] and key[1]==val[1]):
            return True
    return False

def get_nearby_value(data_model,row,col,val):
    shape = data_model.shape
    arr = []
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            if(i>-1 and i<shape[0] and j>-1 and j<shape[1]):
                if((i!=row or j!=col)):
                    if(val<0):
                        arr.append((i, j))
                    elif(data_model[i][j]==val):
                        arr.append((i,j))
    return arr
