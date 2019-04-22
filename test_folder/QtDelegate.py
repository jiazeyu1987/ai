import data_model_folder as dmf




class QtDelegate1:
    def __init__(self):
        pass

    def entry(self):
        #es = self.test_triangle()
        #es = self.test_rectangle()
        es = self.test_circle()
        return es

    def test_rectangle(self):
        e = dmf.get_empty_entity(21, 21)
        center_point = dmf.get_center_point(e)
        entity_rec = dmf.draw_rectangle(e, center_point, 3, 2, 1, False)
        list1 = dmf.step_move_to_point(entity_rec, [1], (0, 0), 1)
        return list1

    def test_circle(self):
        e = dmf.get_empty_entity(100, 100)
        entity_circle = dmf.draw_circle(e, 1, 40)
        # entity_circle = dmf.test_square_21
        # dmf.fill(entity_circle,[1])
        # dmf.shrink(entity_circle, [2])
        # dmf.shrink(entity_circle, [2])
        # dmf.shrink(entity_circle, [2])
        # dmf.shrink(entity_circle, [1])
        # dmf.shrink(entity_circle, 1)
        # dmf.shrink(entity_circle, 1)
        # dmf.shrink(entity_circle, 1)
        # dmf.shrink(entity_circle, 1)
        # dmf.shrink(entity_circle, 1)
        arr = []
        for i in range(3):
            dmf.enlarge(entity_circle, 1)
            arr.append(dmf.clone(entity_circle))

        return arr

        # dmf.enlarge(entity_circle, 1)
        # dmf.enlarge(entity_circle, 1)
        # dmf.enlarge(entity_circle, 1)
        # dmf.reduce(entity_circle, 1)
        # dmf.reduce(entity_circle, 1)
        # dmf.reduce(entity_circle, 1)
        # dmf.reduce(entity_circle, 1)

        # dmf.expand(entity_circle, 1)
        # dmf.expand(entity_circle, 1,2)
        # dmf.is_has_a_hole(entity_circle)
        # dmf.spread(entity_circle, 10)
        # dmf.fill(entity_circle,12)
        # d = dmf.get_hole_number(entity_circle)
        # print("hole:",d)
        # list1 = dmf.step_move_to_point(entity_circle,[1],(0,0))
        # for i in list1:
        #     f.draw_entity(i)
        # print(dmf.has_a_hole(entity_circle,[1,2]))
        # print(entity_circle)


    def test_triangle(self):
        e = dmf.get_empty_entity(50,50)
        center_point = dmf.get_center_point(e)
        entity_triangle = dmf.draw_triangle(e, center_point, 3, 1, "left")
        # dmf.shrink(entity_triangle,[2])
        # dmf.shrink(entity_triangle, [2])
        # dmf.expand(entity_triangle, [2])
        # dmf.expand(entity_triangle, [2])

        list1 = dmf.step_move_to_point(entity_triangle, [1], (0, 0))
        return list1