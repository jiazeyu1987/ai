from utils import  *
class FirstAlgorithm:
    def __init__(self):
        self._lists = []
        pass

    def append(self,list1):
        self._lists.append(list1)

    def analyse(self):
        self._analist()


    def _analist(self):
        #print("\n")
        for i in range(len(self._lists)):
            list1 = self._lists[i]
            self._find_shorts(list1)



    def _find_shorts(self,list1):
        print("((((((((( in short ))))))))))))))))")
        total_marks = self._get_total_marks(list1)
        mark_dict = self._get_mark_dict(total_marks)


        for key in mark_dict:
            print(key,mark_dict[key])

    def _get_mark_dict(self,total_marks):
        dict1 = {}
        for all_marks in total_marks:
            for mark in all_marks:
                if (mark in dict1):
                    dict1[mark] += 1
                else:
                    dict1[mark] = 1
        return dict1

    def _get_total_marks(self,list1):
        arr = []


        for i in range(len(self._lists)):
            if(list1 == self._lists[i]):
                continue

            list2 = self._lists[i]
            arr1 = self._find_shorts_helper(list1,list2)
            arr1 = sorted(arr1,key=lambda list2:len(list2),reverse=True)
            marks,unmarks = self._get_marks(list1,arr1)
            all_marks = []
            for k in marks:
                all_marks.append((k[0],k[1],True))
            for k in unmarks:
                all_marks.append((k[0],k[1],False))
            all_marks = sorted(all_marks,key=lambda mark:mark[0])

            num =0
            for i in all_marks:
                num+=i[1]
            if(num!=len(list1)):
                raise Exception("marks length is wrong")
            arr.append(all_marks)
        return arr


    def _get_marks(self,list1,list_container):
        #print("omark", list_container)

        marks = []
        for arrk in list_container:
            pos_arrs = indexof(list1, arrk)
            for pos_arr in pos_arrs:
                self._add_mark(list1,marks,pos_arr)
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
        return marks,unmarks
        #print("mark:",list1,marks,unmarks)

    def _add_mark(self,list1,marks,mark):
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
                            if(k>1):
                                #print("***",i,j,k)
                                arr.append(list1[i:i+k])
                            break

                j+=1
            i+=1
        return arr



