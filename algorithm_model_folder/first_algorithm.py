from utils import  *
from . import  *
from copy import deepcopy
class FirstAlgorithm:
    def __init__(self):
        self._lists = []
        self._origin = []
        pass

    def append(self,list1):
        self._lists.append(list1)

    def analyse(self):
        return self._analist()


    def _analist(self):
        #print("\n")
        fal_big_list = []
        for i in range(len(self._lists)):
            list1 = self._lists[i]
            fal_list = self._find_shorts(list1)
            fal_big_list = fal_big_list+fal_list
        return self._merge(fal_big_list)


    def _merge(self,fal_big_list):
        chain = FirstAlgorithmChain()
        i=1
        for fal in fal_big_list:
            chain.add_entity_list(fal)


        chain.merge_chains(self._lists)
        return chain


    def _find_shorts(self,list1):
        #print("((((((((( in short ))))))))))))))))")
        total_marks = self._get_total_marks(list1)
        # for k in total_marks:
        #     print(k)
        # return
        mark_dict = self._get_mark_dict(total_marks)
        fallist = self._change_marklist_to_sublist(list1,mark_dict)
        # for k in sublist_dict:
        #     print(k)
        return fallist

        # for key in mark_dict:
        #     print(key,mark_dict[key])for key in mark_dict:
        #     print(key,mark_dict[key])

    def _change_marklist_to_sublist(self,list1,mark_dict):
        #print("mark_dict:",mark_dict)
        fallist = []
        for mark in mark_dict:
            simplelist = []
            show_number = mark_dict[mark]
            if(len(mark)%3!=0):
                raise  Exception("error on _change_marklist_to_sublist")
            for i in range(int(len(mark)/3)):
                start_point = mark[i*3]
                len1 = mark[i*3+1]
                type = mark[i*3+2]
                sublist = list1[start_point:start_point+len1]
                fae = FirstAlgorithmEntity(sublist,type)
                simplelist.append(fae)
            fallist.append(FirstAlgorithmList(simplelist,show_number))
        #print("sublist_dict",sublist_dict)
        return fallist



    def _get_mark_dict(self,total_marks):
        dict1 = {}
        for all_marks2 in total_marks:
            all_marks = all_marks2[0]
            list1 = all_marks2[1]
            list2 = all_marks2[2]
            tmp =()
            for i in range(len(all_marks)):
                tmp = tmp+all_marks[i]
            if (tmp in dict1):
                dict1[tmp].append((list1,list2))
            else:
                dict1[tmp] = [(list1,list2)]
        return dict1

    def _get_total_marks(self,list1):
        arr = []
        for i in range(len(self._lists)):
            if(list1 == self._lists[i]):
                continue
            list2 = self._lists[i]
            arr1 = self._find_shorts_helper(list1,list2)
            #print(arr1,list1,list2)
            marks,unmarks = get_marks(list1,arr1)
            all_marks = self._get_all_marks(marks,unmarks)
            self._check_legal(list1,all_marks)
            arr.append((all_marks,list1,list2))
        return arr

    def _check_legal(self,list1,all_marks):
        num = 0
        for i in all_marks:
            num += i[1]
        if (num != len(list1)):
            raise Exception("marks length is wrong")

    # marks[(0, 2), (3, 9)]
    # unmarks[(2, 1)]
    # all_marks[(0, 2, True), (2, 1, False), (3, 9, True)]
    #
    # marks[(0, 2), (3, 9)]
    # unmarks[(2, 1)]
    # all_marks[(0, 2, True), (2, 1, False), (3, 9, True)]
    #
    # marks[(0, 2), (3, 9)]
    # unmarks[(2, 1)]
    # all_marks[(0, 2, True), (2, 1, False), (3, 9, True)]
    #
    # marks[(0, 2), (3, 9)]
    # unmarks[(2, 1)]
    # all_marks[(0, 2, True), (2, 1, False), (3, 9, True)]
    def _get_all_marks(self,marks,unmarks):
        all_marks = []
        for k in marks:
            all_marks.append((k[0], k[1], True))
        for k in unmarks:
            all_marks.append((k[0], k[1], False))
        all_marks = sorted(all_marks, key=lambda mark: mark[0])
        # print("")
        # print("marks",marks)
        # print("unmarks", unmarks)
        # print("all_marks", all_marks)
        return all_marks





    # list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # list2: [1, 2, 6, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # return_value[[1, 2], [4, 5, 6, 7, 8, 9, 10, 11, 12]]
    #
    # list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # list2: [1, 2, 7, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # return_value[[1, 2], [4, 5, 6, 7, 8, 9, 10, 11, 12]]
    #
    # list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # list2: [1, 2, 8, 4, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # return_value[[1, 2], [4, 5], [4, 5, 6, 7, 8, 9, 10, 11, 12]]
    #
    # list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # list2: [1, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # return_value[[1, 2], [4, 5, 6, 7, 8, 9, 10, 11, 12]]
    def _find_shorts_helper(self,list1,list2):
        #print("\n\n\n")
        arr = []
        i = 0
        j = 0
        while(i<len(list1)):
            j=0
            while(j<len(list2)):
                len1 = len(list1)
                len2 = len(list2)
                subl = min(len1-i,len2-j)
                kapii = 0
                if(list1[i]==list2[j]):
                    kapii = list1[i]
                    for k in range(subl):
                        if list1[i+k]==list2[j+k]:
                            if(i+k==len(list1)-1 or j+k==len(list2)-1):
                                #print("&&&",i,j,k)
                                arr.append(list1[i:i + k+1])
                                #print("NNN:",list1[i:i+k+1])
                                i = i+k
                                j = len(list2)
                                break
                            else:
                                #print("^^^^",i,j,k,subl,len(list1),len2)
                                pass
                        else:
                            if(k>0):
                                #print("***",i,j,k)
                                arr.append(list1[i:i+k])
                            break

                j+=1
            i+=1
        arr = sorted(arr, key=lambda list2: len(list2), reverse=True)
        # print("")
        # print("list1:",list1)
        # print("list2:",list2)
        # print("return_value",arr)
        #print(arr,list1,list2)
        return arr



