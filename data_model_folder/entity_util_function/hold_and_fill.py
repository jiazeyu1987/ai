import data_model_folder as dmf
def is_has_a_hole(entity):
    random_number = dmf.get_random_unexist_value(entity)
    dmf.spread(entity,random_number)
    point2 = dmf.get_point_by_value(entity,0)
    dmf.change_value(entity,random_number,0)
    if(point2!=None):
        return True,point2
    else:
        return None,None


def create_a_hole(entity,arr1):
    pass


def get_hole_number(entity):
    index = 0
    rn_arr = []
    point2 = None
    while(True):
        random_number = dmf.get_random_unexist_value(entity)
        rn_arr.append(random_number)
        if(point2==None):
            dmf.spread(entity, random_number)
        else:
            dmf.spread_by_point(entity,point2,random_number)
        point2 = dmf.get_point_by_value(entity, 0)
        if(point2 != None):
            index+=1
        else:
            for i in rn_arr:
                dmf.change_value(entity,i,0)
            return index


def fill(entity,val):
    while(True):
        f,p = is_has_a_hole(entity)
        if(f):
            dmf.spread_by_point(entity,p,val)
        else:
            break