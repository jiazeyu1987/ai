import  algorithm_model_folder as amf
def test_first_algorithm():
    amf.fa.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.append([1, 2, 6, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.append([1, 2, 7,1, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15])
    amf.fa.append([1, 2, 8,4,5, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.append([1, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.append([1, 2, 4,5,6,7,8, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.append([3,1, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.append([31,  41])
    amf.fa.append([32, 41])
    amf.fa.append([33, 41])
    amf.fa.append([33, 42])


    # amf.fa.append(["我","吃","饭","了"])
    # amf.fa.append(["我", "吃", "苹果", "了"])
    # amf.fa.append(["ta", "吃", "苹果", "了"])
    chain = amf.fa.analyse()


    print(chain)