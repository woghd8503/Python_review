# 함수 기반 주소록 관리 프로그램

import pickle

addressList = []        # 주소를 저장할 리스트

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

def showMenu():
    "메뉴 보여주는 함수"
    print('\n\n')
    print('*' * 10, 'Menu', '*' * 10)
    print('1. Input')
    print('2. Search')
    print('3. Delete')
    print('4. Update')
    print('5. SearchAll')
    print('6. Exit')

def getSelectNum():
    "번호 입력 후 반환하는 함수"
    return int(input("select Menu >> "))

def inputAddress():
    "주소 입력 후 저장 함수"
    print('*** input ***')
    name = input('name >> ')
    age = input('age >> ')
    addr = input('addr >> ')
    address = Address(name, age, addr)
    addressList.append(address)


def searchAddress():
    "주소 검색 함수"
    print('*** search ***')
    name = input("find name >> ")
    for idx, address in enumerate(addressList):
        if address.name == name:
            address.showAddress(idx+1)
            break

def deleteAddress():
    "주소 삭제 함수"
    print('*** delete ***')
    name = input("delete name >> ")
    for idx, address in enumerate(addressList):
        if address.name == name:
            addressList.remove(address)
            break

def updateAddress():
    "주소 변경 함수"
    print('*** update ***')
    uname = input("update name >> ")
    for idx, address in enumerate(addressList):
        if address.name == uname:
            name = input('new name >> ')
            age = input('new age >> ')
            addr = input('new addr >> ')
            address.name = name
            address.age = age
            address.addr = addr
            address.showAddress(idx+1)
            break

def searchAllAddress():
    "모든 주소 검색 함수"
    print('*** searchAll ***')
    for idx, address in enumerate(addressList):
        address.showAddress(idx+1)

def loadAddress():
    "주소록을 파일에서 읽어오는 함수"
    try:
        with open('addressList.bin', 'rb') as f:
            global addressList      # 전역변수를 이 지역에서 사용하겠다
            addressList = pickle.load(f)
    except Exception as e:
        print(e, "- No Such File")

def saveAddress():
    "주소록 리스트의 정보를 파일에 저장하는 함수"
    try:
        with open('addressList.bin', 'wb') as f:
            pickle.dump(addressList, f)
    except Exception as e:
        print(e, "No Saved File")

def exitAddress():
    "주소 프로그램 종료 함수"
    pass

def main():
    "전체 시작 함수"
    loadAddress()
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
            saveAddress()
            break
        else:
            print("메뉴를 잘 못 선택했습니다~")


if __name__ == '__main__':
    main()