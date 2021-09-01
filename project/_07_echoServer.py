# 1)소켓 관련 모듈 임포트
from socket import *

# 2) 접속 수신 소켓 생성
# AF_INET = IPV4(IP주소가 4byte), IPv6(ip주소가 16byte)
# SOCK_STREAM : TCP(신뢰성 있는 통신), UDP(빠른 속도)
serverSock = socket(AF_INET, SOCK_STREAM)

# 3) 프로세스를 종료한 후 바로 재시작해도 주소할당될 수 있는 옵션
# (서버는 보통 이렇게 처리한다)
serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 4) 클라이언트가 연결할 주소를 할당해준다
serverSock.bind(('127.0.0.1', 9000))

# 5) 클라이언트가 접속할 수 있는 준비를 한다
# 클라이언트가 동시에 접속할 때 잠시 대기할 수 있는 공간을 100개 마련한다
serverSock.listen(100)

# 6) 새로운 클라이언트가 접속을 계속 할 수 있도록 무한루프를 돌린다.
while True:
    print('접속 대기중...')
    # 클라이언트가 접속할 때까지 기다리고 있다가 접속하면
    # 통신이 연결된 소켓과 주소를 반환한다
    connSock, connAddr = serverSock.accept()
    print('{0} 접속'.format(connAddr))
    # 연결된 클라이언트와 대화를 계속 할 수 있도록 무한루프를 돌린다.
    while True:
        try:
            s = connSock.recv(1024).decode('utf-8')
            connSock.send(s.encode())
            print('수신 : ' + s)
            if s == '':
                connSock.close()
                print('{0} 정상 접속 종료'.format(connAddr))
                break
        except Exception as e:
            connSock.close()
            print('{0} 비정상 접속 종료'.format(connAddr))
            break