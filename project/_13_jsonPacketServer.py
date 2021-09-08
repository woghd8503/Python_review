from socket import *
import json

def calcArith(cmd, num0, num1):
    result = 0.0
    if cmd == '+':
        result = num0 + num1
    elif cmd == '-':
        result = num0 - num1
    elif cmd == '*':
        result = num0 * num1
    elif cmd == '/':
        result = num0 / num1
    elif cmd == '//':
        result = num0 // num1
    elif cmd == '%':
        result = num0 % num1

    return result

serversock = socket(AF_INET, SOCK_STREAM)
serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serversock.bind(('127.0.0.1', 9000))
serversock.listen(100)

while True:
    print("접속 대기중...")
    connsock, connaddr = serversock.accept()
    print("{} 접속".format(connaddr))
    while True:
        try:
            # 1) 클라이언트로부터 문자열 수신
            strPacket = connsock.recv(1024).decode("utf-8")
            if strPacket == "":
                connsock.close()
                print("{} 정상 접속 종료".format(connaddr))
                break
            print("수신 : " + strPacket)
            # 2) json 문자열 데이터 -> 파이썬 딕셔너리 객체로 변환
            packet = json.loads(strPacket)
            cmd = packet['cmd']
            num0 = packet['num0']
            num1 = packet['num1']
            result = calcArith(cmd, num0, num1)
            # 3) 클라이언트에 응답
            packet = {} # 딕셔너리 객체 생성
            packet['result'] = result
            # 파이썬 딕셔너리 객체 -> json 문자열
            strPacket = json.dumps(packet)
            connsock.send(strPacket.encode())
            print("송신 : " + strPacket)
        except Exception as e:
            print(e)
            connsock.close()
            print("{} Suddenly 접속 종료".format(connaddr))
            break