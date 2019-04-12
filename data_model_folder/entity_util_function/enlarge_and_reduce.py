import data_model_folder as dmf
def enlarge(entity,val):
    rn = dmf.get_random_unexist_value(entity)
    dmf.expand(entity,val,rn)
    dmf.change_value(entity,val,0)
    dmf.change_value(entity,rn,val)
    pass

def reduce(entity,val):
    rn = dmf.get_random_unexist_value(entity)
    dmf.shrink(entity, val, rn)
    dmf.change_value(entity, val, 0)
    dmf.change_value(entity, rn, val)