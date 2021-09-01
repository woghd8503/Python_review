# 1) class란?
# 함수 => 기능, 계산, 절차
# 기능들이 여러 개가 생겼다
# 기능들을 비슷한 종류로 묶고싶다
#
# 한번에 묶어서 관리하면 더 좋겠다
# => 클래스
#
# 변수가 여러개
# 공통분모가 있다.
#
# 마치 사람의 이름, 나이, 주소...
# 묶어서 관리하면 좋겠다
# => 클래스

#사람의 이름, 나이, 주소  (변수)
#      행동, 정보보여주기 (함수)
# 공통분모(같은 종류)
# => 클래스

# a) 필드(변수) + 메서드(함수)들의 집합
# b) 시대가 흐르면서 함수보다 큰 단위가 프로그래밍 환경에 요구됨
# c) 명사(변수) + 동사(메서드)
#     문장의 최소 단위가 1형식 = 주어(명사)+동사 이듯이
#     프로그래밍에서도 변수+메서드의 결합을 통해서
#     프로그래밍의 독립단위를 묘사할 수 있다
# d) 클래스는 현실세계가 독립된 주체들의 상호작용으로 이루어지는
#     것처럼 클래스의 변수인 객체들간의 상호작용으로 프로그래밍을
#     처리할 수 있다.
# e) 현실에서 privacy는 개인이 알아서 처리하고
#     상호 의존할 것은 소통을 통해서 처리하듯이
#     클래스도 내부에서 알아서 처리하는 부분과
#     외부와 상호작용하는 부분으로 나뉘어 진다

# 2) 클래스 제작
# 같은 속성들끼리 묶어서 관리한다
# 클래스는 객체를 만들어서 사용한다

# def add(a, b):
#     return a+b
# def sub(a, b):
#     return a-b
# def mul(a, b):
#     return a*b
# def div(a, b):
#     return a/b

# class Arith:
#     def add(self, a, b):
#         return a+b
#     def sub(self, a, b):
#         return a-b
#     def mul(self, a, b):
#         return a*b
#     def div(self, a, b):
#         return a/b
#
# arith = Arith()     # 객체 생성
# print(arith.add(10, 20))
# print(arith.sub(10, 20))
# print(arith.mul(10, 20))
# print(arith.div(10, 20))


# 3) 클래스 생성자

# self는 C++, C#, Java의 this와 같다
# class Human:
#     def __init__(self, name, age):
#         print("self=", self)
#         self.name = name
#         self.age = age
#     def showInfo(self):
#         print("name:", self.name)
#         print("age:", self.age)
#
# # 객체 = 클래스
# hong = Human("홍다연", 26)  # Human:__init__(hong, "홍다연", 26)
# print("hong=", hong)
# park = Human("박재홍", 32)  # Human:__init__(hong, "박재홍", 32)
# print("hong=", park)
# kim = Human("김도형", 26)   # Human:__init__(hong, "김도형", 26)
# print("hong=", kim)
# hwang = Human("황도경", 26) # Human:__init__(hong, "황도경", 26)
#
# hong.showInfo()     # Human:ShowInfo(hong)
# park.showInfo()     # Human:ShowInfo(park)
# kim.showInfo()      # Human:ShowInfo(kim)
# hwang.showInfo()    # Human:showInfo(hwang)
#
# park.showInfo()

# 4) 클래스 만들기

# class Dog:
#     def __init__(self, name, color):
#         print(name, " 생성자 호출~")
#         self.name = name
#         self.color = color
#     def __del__(self):
#         print(self.name, " 소멸자 호출")
#     def play(self):
#         print("{0}색을 가진 {1}가 즐겁게 뛰어다닌다".format(
#             self.color, self.name))
#
# pipi = Dog("삐삐", "White")
# duggu = Dog("덕구", "Black")
# mery = Dog("메리", "Yellow")
#
# print(pipi.name, pipi.color)
# print(duggu.name, duggu.color)
# print(mery.name, mery.color)
#
# pipi.play()
# duggu.play()
# mery.play()

# 5) 클래스의 재사용성 : 포함
class Computer:
    def __init__(self, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
    def intro(self):
        print("cpu", self.cpu)
        print("gpu", self.gpu)
        print("ram", self.ram)

class Human:
    def __init__(self, name, age, pc):
        self.name = name
        self.age = age
        self.pc = pc
    def intro(self):
        print("name", self.name)
        print("age", self.age)
        self.pc.intro()

albert = Human("알버트", 24, Computer("i7-9700", "RTX-2080", "32G"))
albert.intro()
albert.pc = Computer("i5-5600", "GTX-1060", "16G")
albert.intro()

# 6) 클래스의 재사용성 : 상속
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print("name :", self.name)
        print("age :", self.age)

class WhiteHuman(Human):
    pass

wh = WhiteHuman("백수", 24)
wh.intro()

class Student(Human):
    def __init__(self, name, age, stnum):
        super().__init__(name,age)
        self.stnum = stnum
    def intro(self):
        super().intro()
        print("stnum :", self.stnum)
    def study(self):
        print(self.name, "학생이 열심히 공부한다")

# st0 = Student("홍길동", 33, "1024")
# st0.intro()
# st0.study()