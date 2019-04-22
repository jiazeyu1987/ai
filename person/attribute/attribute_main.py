class AttributeMain:
    def __init__(self,perception_main):
        self._energy =100
        self._food = 100
        self._water = 100
        self._stomach = 50
        self._perception_main = perception_main
        self.die = False
        pass


    def update(self):
        self.set_food(self._food-20)
        print("self.food:",str(self._food))


    def set_food(self,value):
        if(self._food<-200):
            self.die = True

        self._food = value
        if(self._food<0):
            self._perception_main.perception_food.OnHunger(4)
        elif(self._food<20):
            self._perception_main.perception_food.OnHunger(3)
        elif(self._food<40):
            self._perception_main.perception_food.OnHunger(2)
        elif(self._food<60):
            self._perception_main.perception_food.OnHunger(1)

        if(self._food>100):
            self._perception_main.perception_food.OnFull(1)
        elif (self._food > 120):
            self._perception_main.perception_food.OnFull(2)
        elif (self._food > 140):
            self._perception_main.perception_food.OnFull(3)
        elif (self._food > 160):
            self._perception_main.perception_food.OnFull(4)