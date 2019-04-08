import numpy as np
import math
import time

def is_point_position_legal(entity,point):
    if(point[0]<0 or point[1]<0 or point[0]>entity.shape[0]-1 or point[1]>entity.shape[1]-1):
        return False
    return True

def connect_point(entity,point1,point2,val):
    #(entity, point1, val)
    #draw_point(entity, point2, val)
    width = abs(point2[1] - point1[1])
    height = abs(point2[0]-point1[0])
    if(width>height):
        for i in range(width+1):
            minW = min(point2[1],point1[1])
            minH = min(point2[0],point1[0])
            pointW = i
            pointH = round(height/width*i)

            point3 = (minH+pointH,minW+pointW)
            draw_point(entity,point3,val)
    else:
        for i in range(height+1):
            minW = min(point2[1],point1[1])
            minH = min(point2[0],point1[0])
            pointW = i
            pointH = round(width/height*i)
            point3 = (minH+pointH,minW+pointW)
            draw_point(entity,point3,val)

def min(a,b):
    if(a<b):
        return a
    return b

def max(a,b):
    if(a>b):
        return a
    return b

def draw_oblique_line(entity,start_point,direction,len1,val):
    old_point = None
    draw_point(entity, start_point, val)
    len1 -= 1
    if(direction == "up_right"):
        old_point = start_point
        for i in range(0,len1):
            new_point = (old_point[0]-1,old_point[1]+1)
            draw_point(entity,new_point,val)
            old_point = new_point
    elif(direction == "down_right"):
        old_point = start_point
        for i in range(0, len1):
            new_point = (old_point[0] + 1, old_point[1] + 1)
            draw_point(entity, new_point, val)
            old_point = new_point
    elif (direction == "down_left"):
        old_point = start_point
        for i in range(0, len1):
            new_point = (old_point[0] + 1, old_point[1] - 1)
            draw_point(entity, new_point, val)
            old_point = new_point
    elif (direction == "up_left"):
        old_point = start_point
        for i in range(0, len1):
            new_point = (old_point[0] - 1, old_point[1] - 1)
            draw_point(entity, new_point, val)
            old_point = new_point
    return old_point

def get_center_point(entity):
    shape = entity.shape
    return ((int)((shape[0] - 1) / 2), (int)((shape[1] - 1) / 2))

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

def draw_point(entity,point1,val):
    entity[point1[0],point1[1]]=val

def is_near(p1,p2):
    return math.fabs(p1[0]-p2[0])<2 and math.fabs(p1[1]-p2[1])<2

## 0 1 2
## 3 X 5
## 6 7 8
def in_point_position(entity,source_point,dest_point,pos_arr):
    for i in pos_arr:
        if source_point == get_point_by_position(entity,dest_point,i):
            return True
    return False

def get_point_position(entity,source_point,dest_point):
    di = -1
    for i in range(9):
        if (i != 4 and in_point_position(entity,source_point,dest_point,[i])):
            di = i
            break
    return di

def get_point_by_position(entity,outer_point,position):
    return_point = None
    if (position == 0):
        return_point = (outer_point[0] - 1, outer_point[1] - 1)
    elif (position == 1):
        return_point = (outer_point[0] - 1, outer_point[1])
    elif (position == 2):
        return_point = (outer_point[0] - 1, outer_point[1] + 1)
    elif (position == 3):
        return_point = (outer_point[0], outer_point[1] - 1)
    elif (position == 5):
        return_point = (outer_point[0], outer_point[1] + 1)
    elif (position == 6):
        return_point = (outer_point[0] + 1, outer_point[1] - 1)
    elif (position == 7):
        return_point = (outer_point[0] + 1, outer_point[1])
    elif (position == 8):
        return_point = (outer_point[0] + 1, outer_point[1] + 1)
    else:
        raise Exception(position)
    return return_point

def get_value(entity,point):
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


def _expand_point(entity,point,point_list):
    row = point[0]
    col = point[1]
    arr = []
    arr=[(row-1,col),(row+1,col),(row,col-1),(row,col+1)]
    for v in arr:
        if(entity[v[0]][v[1]]==0):
            entity[v[0]][v[1]]=2

def get_entity_point(entity,val):
    shape = entity.shape
    arr = []
    for i in range(shape[0]):
        for j in range(shape[1]):
            if(entity[i][j]==val):
                arr.append((i,j))
    return arr







def get_distance(point1,point2):
    return math.sqrt((point2[1]-point1[1])*(point2[1]-point1[1])+(point2[0]-point1[0])*(point2[0]-point1[0]))

def draw_point(entity,point1,val):
    entity[point1[0],point1[1]]=val

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
    shape = data_model.shape
    row = shape[0]
    col = shape[1]
    for i in range(row):
        for j in range(col):
            if(data_model[i][j]!=0):
                if(is_closed_item(data_model,i,j)):
                    pass
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
