from . import *
def create_perception(type,sub_type=None):
    if(type==TOUCHING):
        return PerceptionTouching(sub_type)
    else:
        raise Exception("123")