def indexof(parent_list,child_list):
    if(parent_list==None or child_list==None or (child_list)==0 or len(parent_list)==0):
        raise Exception("eror in indexof")

    pos_arr=[]
    for i in range(len(parent_list)):
        if(parent_list[i]==child_list[0]):
            pos_arr.append(i)
    #print("**",pos_arr)
    pos_len_arr = []
    for i in pos_arr:
        len1 = 0
        for j in range(i,len(parent_list)):
            if(j-i>len(child_list)-1):
                break
            if parent_list[j] == child_list[j-i]:
                len1+=1
                if(len1==len(child_list)):
                    pos_len_arr.append((i,len1))
            else:
                break
    return pos_len_arr


# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# list_container[[4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2]]
# marks[(0, 2), (3, 9)]
# unmarks[(2, 1)]
#
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# list_container[[4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2]]
# marks[(0, 2), (3, 9)]
# unmarks[(2, 1)]
#
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# list_container[[4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2], [4, 5]]
# marks[(0, 2), (3, 9)]
# unmarks[(2, 1)]
#
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# list_container[[4, 5, 6, 7, 8, 9, 10, 11, 12], [1, 2]]
# marks[(0, 2), (3, 9)]
# unmarks[(2, 1)]
def get_marks(list1,list_container):
    #print("omark", list_container)

    marks = []
    for arrk in list_container:
        pos_arrs = indexof(list1, arrk)
        for pos_arr in pos_arrs:
            add_mark(list1,marks,pos_arr)
    marks = sorted(marks,key=lambda mark:mark[0])
    index = 0
    unmarks = []
    for i in range(len(marks)):
        mark = marks[i]
        if(index<mark[0]):
            unmarks.append((index,mark[0]-index))
            index=mark[0]+mark[1]
        elif(index==mark[0]):
            index = mark[0] + mark[1]
    if(index<len(list1)):
        unmarks.append((index,len(list1)-index))
    # print("")
    # print("list1:",list1)
    # print("list_container",list_container)
    # print("marks",marks)
    # print("unmarks",unmarks)

    marks =sorted(marks,key=lambda mark:mark[0])
    unmarks = sorted(unmarks, key=lambda mark: mark[0])
    return marks,unmarks
    #print("mark:",list1,marks,unmarks)

def add_mark(list1,marks,mark):
    Repeat = False
    for i in range(mark[0],mark[0]+mark[1]):
        for unit in marks:
            for j in range(unit[0],unit[0]+unit[1]):
                if(i==j):
                    Repeat = True
    if(Repeat):
        return
    else:
        marks.append(mark)