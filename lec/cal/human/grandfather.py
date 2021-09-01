
class cgrandfather:
    "할아버지 클래스"
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.money = money


    def intro(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("money : ",self.money)

    def happy(self):
        print("돈 {0}으로 인생이 행복하다".format(self.money))
