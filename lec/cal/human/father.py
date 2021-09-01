from .grandfather import cgrandfather

class cfather(cgrandfather):
    "아버지 클래스"
    def __init__(self, name,age,money,knowledge):
        super().__init__(name,age,money)
        self.knowledge = knowledge

    def intro(self):
        super().intro()
        print("knowledge :",self.knowledge)

    def study(self):
        print(self.knowledge +"를 얻기 위해 공부를 한다")