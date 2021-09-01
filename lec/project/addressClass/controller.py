from .dao import *
from .vo import *


# ***************** 전역변수 start ********************
g_SqliteAddressDao = SqliteAddressDao('address.db')
# ***************** 전역변수 end   ********************

class AddressManager:
    def inputAddress(self):
        "주소 입력 후 저장 함수"
        print('*** input ***')
        name = input('name >> ')
        age = input('age >> ')
        addr = input('addr >> ')
        address = Address(name, age, addr)
        g_SqliteAddressDao.inputAddress(tableName='address', address=address)

    def searchAddress(self):
        "주소 검색 함수"
        print('*** search ***')
        name = input("find name >> ")
        addressOne = g_SqliteAddressDao.searchAddress(tableName='address', name=name)
        address = Address(addressOne[1], addressOne[2], addressOne[3])
        address.showAddress(addressOne[0])

    def deleteAddress(self):
        "주소 삭제 함수"
        print('*** delete ***')
        name = input("delete name >> ")
        g_SqliteAddressDao.deleteAddress(tableName='address', name=name)

    def updateAddress(self):
        "주소 변경 함수"
        print('*** update ***')
        uname = input("update name >> ")
        name = input('new name >> ')
        age = input('new age >> ')
        addr = input('new addr >> ')
        address = Address(name, age, addr)
        g_SqliteAddressDao.updateAddress(tableName='address', fname=uname, address=address)

    def searchAllAddress(self):
        "모든 주소 검색 함수"
        print('*** searchAll ***')
        addressList = g_SqliteAddressDao.searchAllAddress(tableName='address')
        for addr in addressList:
            address = Address(addr[1], addr[2], addr[3])
            address.showAddress(addr[0])