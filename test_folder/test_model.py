import  data_model_folder as dmf
import tkinter
import threading
import time
def test_model2():
    f = dmf.TKInterMain()
    th = threading.Thread(target=fun1, args=(f,))
    th.setDaemon(True)  # 守护线程
    th.start()
    f.start()

def fun1(f):
    #test_rectangle(f)
    #test_circle(f)
    test_triangle(f)

def test_rectangle(f):
    e = dmf.get_empty_entity(21, 21)
    center_point = dmf.get_center_point(e)
    entity_rec = dmf.draw_rectangle(e, center_point, 3, 2, 1,False)
    list1 = dmf.step_move_to_point(entity_rec,[1],(0,0),1)



    for i in list1:
        time.sleep(.5)
        f.draw_entity(i)
    #dmf.spread(entity_rec,10)
    #print(entity_rec)

def test_circle(f):
    e = dmf.get_empty_entity(21, 21)
    entity_circle = dmf.draw_circle(e,1,5)
    #entity_circle = dmf.test_square_21
    #dmf.fill(entity_circle,[1])
    # dmf.shrink(entity_circle, [2])
    # dmf.shrink(entity_circle, [2])
    # dmf.shrink(entity_circle, [2])
    #dmf.shrink(entity_circle, [1])
    # dmf.shrink(entity_circle, 1)
    # dmf.shrink(entity_circle, 1)
    # dmf.shrink(entity_circle, 1)
    # dmf.shrink(entity_circle, 1)
    # dmf.shrink(entity_circle, 1)

    # dmf.enlarge(entity_circle, 1)
    # dmf.enlarge(entity_circle, 1)
    # dmf.enlarge(entity_circle, 1)
    # dmf.enlarge(entity_circle, 1)
    # dmf.reduce(entity_circle, 1)
    # dmf.reduce(entity_circle, 1)
    # dmf.reduce(entity_circle, 1)
    # dmf.reduce(entity_circle, 1)

    # dmf.expand(entity_circle, 1)
    #dmf.expand(entity_circle, 1,2)
    #dmf.is_has_a_hole(entity_circle)
    #dmf.spread(entity_circle, 10)
    #dmf.fill(entity_circle,12)
    #d = dmf.get_hole_number(entity_circle)
    #print("hole:",d)
    # list1 = dmf.step_move_to_point(entity_circle,[1],(0,0))
    # for i in list1:
    #     f.draw_entity(i)
    #print(dmf.has_a_hole(entity_circle,[1,2]))
    print(entity_circle)



def test_triangle(f):
    e = dmf.get_empty_entity(121, 121)
    center_point = dmf.get_center_point(e)
    entity_triangle = dmf.draw_triangle(e, center_point, 3, 1,"left")
    #dmf.shrink(entity_triangle,[2])
    #dmf.shrink(entity_triangle, [2])
    # dmf.expand(entity_triangle, [2])
    # dmf.expand(entity_triangle, [2])

    list1 = dmf.step_move_to_point(entity_triangle, [1], (0, 0))
    for i in list1:
        f.draw_entity(i)

