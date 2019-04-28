class ActionBase:
    def __init__(self,value):
        self.value = value
        pass

    def get_value(self):
        return self.value

    @classmethod
    def unique_flag(cls):
        raise Exception("dkfal;dskfjalsdkf")