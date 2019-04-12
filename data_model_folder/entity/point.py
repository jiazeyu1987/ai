import data_model_folder as dmf
def get_random_unexist_value(entity,val = 10):
    shape = entity.shape
    arr = []
    for i in range(shape[0]):
        for j in range(shape[1]):
            if(entity[i][j]!=0 and (entity[i][j] in arr)==False):
                arr.append(entity[i][j])
    for i in range(val,1000):
        if((i in arr)==False):
            return i

    return -1

def remove_point_from_list(list1,point1):
    arr = []
    for i in list1:
        if(i[0]==point1[0] and i[1]==point1[1]):
            pass
        else:
            arr.append(i)
    return arr

def get_point_by_value(entity,val):
    for i in range(entity.shape[0]):
        for j in range(entity.shape[1]):
            if(entity[i][j]==val):
                return (i,j)
    return None

def get_left_up_point(entity,valist):
    arr = []
    for i in range(entity.shape[0]):
        for j in range(entity.shape[1]):
            if(entity[i][j] in valist):
                arr.append((i,j))
    arr = sorted(arr,key=lambda val:(val[0],val[1]))
    if(len(arr)>0):
        return arr[0]

def get_right_down_point(entity,valist):
    arr = []
    for i in range(entity.shape[0]):
        for j in range(entity.shape[1]):
            if(entity[i][j] in valist):
                arr.append((i, j))
    arr = sorted(arr,key=lambda val:(val[0],val[1]),reverse=True)
    if(len(arr)>0):
        return arr[0]

def is_point_position_legal(entity,point):
    if(point[0]<0 or point[1]<0 or point[0]>entity.shape[0]-1 or point[1]>entity.shape[1]-1):
        return False
    return True

def get_center_point(entity):
    shape = entity.shape
    return ((int)((shape[0] - 1) / 2), (int)((shape[1] - 1) / 2))

def draw_point(entity,point1,val):
    entity[point1[1],point1[0]]=val
def draw_point_reverse(entity,point1,val):
    entity[point1[0],point1[1]]=val


## 0 1 2
## 3 X 5
## 6 7 8
def in_point_position(entity,source_point,dest_point,pos_arr):
    for i in pos_arr:
        if source_point == get_point_by_position(dest_point,i):
            return True
    return False

def get_point_position(entity,source_point,dest_point):
    di = -1
    for i in range(9):
        if (i != 4 and in_point_position(entity,source_point,dest_point,[i])):
            di = i
            break
    return di

def get_point_by_position(outer_point,position):
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
