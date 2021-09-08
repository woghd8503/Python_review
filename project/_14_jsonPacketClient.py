from socket import *
import json

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 9000))

# 사칙연산 데이터를 입력받고
# json 문자열로 전송해서
# 결과를 응답받는다
while True:
    num0 = int(input("첫번째 숫자 입력 >> "))
    num1 = int(input("두번째 숫자 입력 >> "))
    op = input("연산자 입력 >> ")

    packet = {} # 딕셔너리 객체 생성
    packet['cmd'] = op
    packet['num0'] = num0
    packet['num1'] = num1
    # 파이썬 객체 -> json 문자열 변환
    strPacket = json.dumps(packet)
    clientsock.send(strPacket.encode())
    # 서버가 보내온 json 문자열 수신
    s = clientsock.recv(1024).decode("utf-8")
    # json문자열 -> 파이썬 딕셔너리 객체로 변환
    strPacket = json.loads(s)
    print("result=", strPacket['result'])

clientsock.close()








