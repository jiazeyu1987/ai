class FirstAlgorithmEntity:
    def __init__(self,value,know_or_not,show_times=-1):
        self._value = value
        self._known = know_or_not
        self._show_times = show_times
        pass

    def __str__(self):
        return "<FirstAlgorithmEntity "+str(self._value)+" - "+str(self._known)+">"

    def is_known(self):
        return self._known

    def get_value(self):
        return self._value