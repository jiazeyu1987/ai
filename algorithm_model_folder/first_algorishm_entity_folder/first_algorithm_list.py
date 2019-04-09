class FirstAlgorithmList:
    def __init__(self,list1,show_times):
        self._list = list1
        self._show_times = show_times
        pass


    def __str__(self):
        print("\n\nFirstAlgorithmList Start")
        for k in self._list:
            print(k)
        print("show_times:",self._show_times)
        print("FirstAlgorithmList End\n")
        return ""
