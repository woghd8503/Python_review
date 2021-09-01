from .father import cfather

class cmy(cfather):
    "나 클래스"
    def __init__(self,name,age,money,knowledge,power):
        super().__init__(name,age,money,knowledge)
        self.power = power

    def intro(self):
        super().intro()
        print("power : ",self.power)

    def health(self):
        print(self.power +"를 돕기 위해 운동을 한다.")