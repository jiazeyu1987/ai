class FirstAlgorithmList:
    def __init__(self,list1,show_times):
        self._list = list1
        self._show_times = show_times
        pass


    def __str__(self):
        print("\n\nFirstAlgorithmList Start")
        for i in range(len(self._list)):
            print(i)
            print(self._list[i])
        print("show_times:")
        print(self._show_times)
        print("FirstAlgorithmList End\n")
        return ""
