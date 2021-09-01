# 함수 기반 주소록 관리 프로그램

import sqlite3

# Dao : Data Access Object
class SqliteAddressDao:
    "sqlite에 주소록 입출력을 담당하는 클래스"
    def __init__(self, fileName):
        self.conn = sqlite3.connect(fileName)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def inputAddress(self, tableName, address):
        sql = """
            INSERT INTO {0}(name, age, addr) VALUES('{1}','{2}','{3}')
        """.format(tableName, address.name, address.age, address.addr)
        self.cursor.execute(sql)
        self.conn.commit()

    def searchAddress(self, tableName, name):
        sql = """
            SELECT * FROM {0} WHERE name='{1}'
        """.format(tableName, name)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def deleteAddress(self, tableName, name):
        sql = """
            DELETE FROM {0} WHERE name='{1}'
        """.format(tableName, name)
        self.cursor.execute(sql)
        self.conn.commit()

    def updateAddress(self, tableName, fname, address):
        sql = """
            UPDATE {0} SET name='{1}', age='{2}', addr='{3}'
             WHERE name='{4}'
        """.format(tableName, address.name, address.age, address.addr, fname)
        self.cursor.execute(sql)
        self.conn.commit()

    def searchAllAddress(self, tableName):
        sql = """
            SELECT * FROM {0}
        """.format(tableName)
        self.cursor.execute(sql)
        return self.cursor.fetchall()


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
    g_SqliteAddressDao.inputAddress(tableName='address', address=address)


def searchAddress():
    "주소 검색 함수"
    print('*** search ***')
    name = input("find name >> ")
    addressOne = g_SqliteAddressDao.searchAddress(tableName='address', name=name)
    address = Address(addressOne[1], addressOne[2], addressOne[3])
    address.showAddress(addressOne[0])

def deleteAddress():
    "주소 삭제 함수"
    print('*** delete ***')
    name = input("delete name >> ")
    g_SqliteAddressDao.deleteAddress(tableName='address', name=name)

def updateAddress():
    "주소 변경 함수"
    print('*** update ***')
    uname = input("update name >> ")
    name = input('new name >> ')
    age = input('new age >> ')
    addr = input('new addr >> ')
    address = Address(name, age, addr)
    g_SqliteAddressDao.updateAddress(tableName='address', fname=uname, address=address)

def searchAllAddress():
    "모든 주소 검색 함수"
    print('*** searchAll ***')
    addressList = g_SqliteAddressDao.searchAllAddress(tableName='address')
    for addr in addressList:
        address = Address(addr[1], addr[2], addr[3])
        address.showAddress(addr[0])

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
            print("메뉴를 잘 못 선택했습니다~")


# ***************** 전역변수 start ********************
g_SqliteAddressDao = SqliteAddressDao('address.db')
# ***************** 전역변수 end   ********************

if __name__ == '__main__':
    main()