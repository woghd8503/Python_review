
class Address:
    "주소 객체를 생성할 클래스"
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr

    def showAddress(self, idx):
        print('+' * 10, end='')
        print(idx, end='')
        print('+' * 10)
        print('name :', self.name)
        print('age :', self.age)
        print('addr :', self.addr)


