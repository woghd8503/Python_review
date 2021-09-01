from socket import *

# 소켓을 생성
clientSock = socket(AF_INET, SOCK_STREAM)
# 서버의 주소로 접속/연결
clientSock.connect(('127.0.0.1', 9000))

while True:
    s = input('전송 문자열 >> ')
    if s == '<stop>':
        break
    clientSock.send(s.encode())
    s = clientSock.recv(1024).decode('utf-8')
    print('서버로부터 수신 : ' + s)