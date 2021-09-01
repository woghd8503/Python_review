# 함수 기반 주소록 관리 프로그램

import pickle

addressDict = {}        # 주소를 저장할 리스트

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
    name = input('name >> ').title()
    age = input('age >> ')
    addr = input('addr >> ')
    addressDict[name] = "age: " + age, "addr: " + addr;

def searchAddress():
    "주소 검색 함수"
    print('*** search ***')
    name = input("find name >> ").title()
    result = addressDict.get(name, 'There is no information')
    print(f'{name}:', result)

def deleteAddress():
    "주소 삭제 함수"
    print('*** delete ***')
    name = input("delete name >> ").title()
    if name not in addressDict.keys():
        print('There is no information')
        return
    else:
        ask = input(f"{name} Do you really want to delete the information(y): ").lower()
        if ask == 'y':
            del addressDict[name]
            print(f'Completely delete {name}')
        else:
            print(f'It has not been deleted')

def updateAddress():
    "주소 변경 함수"
    print('*** update ***')
    name = input("update name >> ")
    if name not in addressDict.keys():
        print(f'There dose not exist {name}')
        return
    else:
        age = input('new age >> ')
        addr = input('new addr >> ')
        addressDict[name] = age, addr;
        print(f'{name} has been updated ***')

def searchAllAddress():
    "모든 주소 검색 함수"
    print('*** searchAll ***')
    for idx, address in addressDict.items():
        print(f'{idx}: {address}')

def exitAddress():
    "주소 프로그램 종료 함수"
    pass

def main():
    "전체 시작 함수"
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
            break
        else:
            print("You selected wrong number")


if __name__ == '__main__':
    main()