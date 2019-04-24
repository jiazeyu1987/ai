class PerceptionBase:
    def __init__(self,value,source="inner"):
        self.value = value
        self.source = source
        self.degree = -1
        pass

    def __str__(self):
        return str(self.source)+"@"+self.unique_flag()+"@"+str(self.degree)


    def equal(self,perception):
        return self.value == perception.value

    @classmethod
    def unique_flag(cls):
        raise Exception("dkfal;dskfjalsdkf")
