import data_model_folder as dmf

def move_to_point(entity,vallist,point1):
    left_point = dmf.get_left_up_point(entity, vallist)
    deltaX = point1[0]-left_point[0]
    deltaY = point1[0]-left_point[1]

    arr = []
    for i in range(entity.shape[0]):
        for j in range(entity.shape[1]):
            if(entity[i][j] in vallist):
                if(j+deltaY>-1 and i+deltaX>-1 and j+deltaY<entity.shape[1] and i+deltaX<entity.shape[0]):
                    arr.append((j+deltaY,i+deltaX))

    new_entity = dmf.get_empty_entity(entity.shape[0],entity.shape[1])
    for k in arr:
        dmf.draw_point(new_entity,k,vallist[0])
    return new_entity

def step_move_to_point(entity,vallist,point1,step=1):
    left_point = dmf.get_left_up_point(entity,vallist)
    #right_point = dmf.get_right_down_point(entity,vallist)
    deltaX = abs(point1[0]-left_point[0])
    deltaY = abs(point1[1]-left_point[1])
    simboX = -1
    if(point1[0]-left_point[0]>0):
        simboX = 1
    simboY = -1
    if (point1[1] - left_point[1] > 0):
        simboY = 1
    deltaMax =max(deltaX,deltaY)
    entitylist = []
    for i in range(0,deltaMax+1,step):
        stepX = deltaX/deltaMax
        stepY = deltaY/deltaMax
        newX = left_point[0]+stepX*simboX*i
        newY = left_point[1]+stepY*simboY*i
        iX = int(newX)
        iY = int(newY)
        newe = move_to_point(entity,[1],(iX,iY))
        entitylist.append(newe)
    return entitylist


def step_move_to_point(entity,vallist,point1,step=1):
    left_point = dmf.get_left_up_point(entity,vallist)
    #right_point = dmf.get_right_down_point(entity,vallist)
    deltaX = abs(point1[0]-left_point[0])
    deltaY = abs(point1[1]-left_point[1])
    simboX = -1
    if(point1[0]-left_point[0]>0):
        simboX = 1
    simboY = -1
    if (point1[1] - left_point[1] > 0):
        simboY = 1
    deltaMax =max(deltaX,deltaY)
    entitylist = []
    for i in range(0,deltaMax+1,step):
        stepX = deltaX/deltaMax
        stepY = deltaY/deltaMax
        newX = left_point[0]+stepX*simboX*i
        newY = left_point[1]+stepY*simboY*i
        iX = int(newX)
        iY = int(newY)
        newe = move_to_point(entity,[1],(iX,iY))
        entitylist.append(newe)
    return entitylist
