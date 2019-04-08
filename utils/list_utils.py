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