print_flag = True
def printt(self, *args, sep=' ', end='\n', file=None):
    if(print_flag):
        str1 = self.__str__()
        for i in range(len(args)):
            str2 = ((args[i]).__str__())
            str1 = str1 + " "+str2
        print(str1)
    else:
        pass
