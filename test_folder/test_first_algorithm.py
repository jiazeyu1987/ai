import  algorithm_model_folder as amf
def test_first_algorithm():
    amf.fa.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.append([1, 2, 6, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.append([1, 2, 7,1, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15])
    amf.fa.append([1, 2, 8,4,5, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.append([1, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    amf.fa.analyse()