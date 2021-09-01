

class AddressView:
    # 클래스 메서드는 C++/C#의 static 메서드와 동일하다
    # 객체의 소속이 아니라 클래스 소속이 된다
    # 객체를 만들지 않아도 클래스를 통해 바로 호출할 수 있는 메서드가 된다.
    @classmethod
    def showMenu(cls):
        "메뉴 보여주는 함수"
        print('\n\n')
        print('*' * 10, 'Menu', '*' * 10)
        print('1. Input')
        print('2. Search')
        print('3. Delete')
        print('4. Update')
        print('5. SearchAll')
        print('6. Exit')

    @classmethod
    def getSelectNum(cls):
        "번호 입력 후 반환하는 함수"
        return int(input("select Menu >> "))