from .view import *
from .controller import *

addressManager = AddressManager()

def main():
    "전체 시작 함수"
    while True:
        AddressView.showMenu()
        num = AddressView.getSelectNum()
        if num == 1:
            addressManager.inputAddress()
        elif num == 2:
            addressManager.searchAddress()
        elif num == 3:
            addressManager.deleteAddress()
        elif num == 4:
            addressManager.updateAddress()
        elif num == 5:
            addressManager.searchAllAddress()
        elif num == 6:
            break
        else:
            print("메뉴를 잘 못 선택했습니다~")



