class PerceptionBase:
    def __init__(self,main_type,source=None):
        self.main_type = main_type
        self.source = source
        pass

    def __str__(self):
        return self.main_type