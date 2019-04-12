import  data_model_folder as dmf
import  time
def spread(entity,val):
    point1 = dmf.get_a_outter_point(entity)
    spread_by_point(entity,point1,val)

def spread_by_point(entity,point1,val):
    if (point1 == None):
        return
    dmf.draw_point_reverse(entity, (point1[0], point1[1]), val)
    _spread_helper(entity, point1, val)

def _spread_helper(entity,point1,val):
    point_list = dmf.get_neighbor_of_val_0(entity,point1)
    for i in point_list:
        dmf.draw_point_reverse(entity,i,val)
    for i in point_list:
        pl = dmf.get_neighbor_of_val_0(entity,i)
        if(len(pl)>0):
            for j in pl:
                _spread_helper(entity,j,val)

