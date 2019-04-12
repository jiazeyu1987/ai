import data_model_folder as dmf
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
            dmf.draw_point(entity,point3,val)
    else:
        for i in range(height+1):
            minW = min(point2[1],point1[1])
            minH = min(point2[0],point1[0])
            pointW = i
            pointH = round(width/height*i)
            point3 = (minH+pointH,minW+pointW)
            dmf.draw_point(entity,point3,val)


def connect_two_point(entity,point1,point2,val):
    dx = abs(point2[0]-point1[0])
    dy = abs(point2[1]-point1[1])
    max1 = max(dx,dy)
    deltaX = dx/max1
    deltaY = dy/max1

    px = -1
    if(point2[0]>point1[0]):
        px = 1

    py = -1
    if (point2[1] > point1[1]):
        py = 1
    for i in range(max1):
        tx = point1[0]+deltaX*px*i
        ty = point1[1] + deltaY * py*i
        ix = int(tx)
        iy = int(ty)
        dmf.draw_point(entity,(ix,iy),val)


def draw_oblique_line(entity,start_point,direction,len1,val):
    old_point = None
    dmf.draw_point(entity, start_point, val)
    len1 -= 1
    if(direction == "up_right"):
        old_point = start_point
        for i in range(0,len1):
            new_point = (old_point[0]+1,old_point[1]-1)
            dmf.draw_point(entity,new_point,val)
            print("A",new_point)
            old_point = new_point
    elif(direction == "down_right"):
        old_point = start_point
        for i in range(0, len1):
            new_point = (old_point[0] + 1, old_point[1] + 1)
            dmf.draw_point(entity, new_point, val)
            old_point = new_point
    elif (direction == "down_left"):
        old_point = start_point
        for i in range(0, len1):
            new_point = (old_point[0] - 1, old_point[1] + 1)
            dmf.draw_point(entity, new_point, val)
            old_point = new_point
    elif (direction == "up_left"):
        old_point = start_point
        for i in range(0, len1):
            new_point = (old_point[0] - 1, old_point[1] - 1)
            dmf.draw_point(entity, new_point, val)
            old_point = new_point
    return old_point