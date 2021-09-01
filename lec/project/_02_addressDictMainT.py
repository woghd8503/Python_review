# 함수 기반 주소록 관리 프로그램

import pickle

addressDict = {}    # 주소를 저장할 딕셔너리

class Address:
    "주소 객체를 생성할 클래스"
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr

    def showAddress(self, idx=0):
        print('+' * 10, end='')
        print(idx, end='')
        print('+' * 10)
        print("name :", self.name)
        print("age :", self.age)
        print("addr :", self.addr)

def showMenu():
    print('\n\n')
    print('*' * 10, 'Menu', '*' * 10)
    print('1. Input')
    print('2. Search')
    print('3. Delete')
    print('4. Update')
    print('5. SearchAll')
    print('6. Exit')

def getSelectNum():
    return int(input("select Menu >> "))

def inputAddress():
    print("*** input ***")
    name = input("name >> ")
    age = input("age >> ")
    addr = input("addr >> ")
    address = Address(name, age, addr)
    addressDict[name] = address

def searchAddress():
    print("*** search ***")
    name = input("find name >> ")
    try:
        addr = addressDict[name]
        addr.showAddress()
    except Exception as e:
        print(e, "Not Found")

def deleteAddress():
    print("*** delete ***")
    name = input("delete name >> ")
    addressDict.pop(name)

def updateAddress():
    print("*** update ***")
    uname = input("update name >> ")
    try:
        address = addressDict.pop(uname)
        name = input("new name >> ")
        age = input("new age >> ")
        addr = input("new addr >> ")
        address.name = name
        address.age = age
        address.addr = addr
        addressDict[name] = address
    except Exception as e:
        print(e, "Not Found")


def searchAllAddress():
    print("*** searchAll ***")
    idx = 0
    for addr in addressDict.values():
        addr.showAddress(idx)
        idx += 1

def loadAddress():
    try:
        with open('addressDict.bin', 'rb') as f:
            global addressDict  # 전역 변수를 함수 내에서 사용하겠다
            addressDict = pickle.load(f)
    except:
        print("No Such File")

def saveAddress():
    try:
        with open('addressDict.bin', 'wb') as f:
            pickle.dump(addressDict, f)
    except:
        print("No Saved File")

def main():
    loadAddress()  # 파일로부터 addressDict 복원
    while True:
        showMenu()
        num = getSelectNum()
        if num == 1:
            inputAddress()
        elif num == 2:
            searchAddress()
        elif num == 3:
            deleteAddress()
        elif num == 4:
            updateAddress()
        elif num == 5:
            searchAllAddress()
        elif num == 6:
            saveAddress() # 종료 전에 addressDict를 파일에 저장
            break
        else:
            print("메뉴를 잘못 선택했습니다")
    pass


# 코드의 실행하는 시작위치 표시할 때
if __name__ == '__main__':
    main()