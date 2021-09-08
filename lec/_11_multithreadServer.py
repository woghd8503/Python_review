import socket
from socketserver import ThreadingTCPServer, StreamRequestHandler

PORT = 9000

clientList = [] # 클라이언트 connSock을 저장할 리스트

def sendAll(msg, exceptSock):
    "exceptSock을 제외하고, 연결된 모든 클라이언트에 데이터를 전송"
    for clientSock in clientList:
        if clientSock != exceptSock:
            clientSock.send(msg.encode())

class RequestHandler(StreamRequestHandler):
    # 클라이언트 접속시 스레드가 생성되고
    # 해당 스레드는 handle 메서드를 동작시킨다
    def handle(self):
        print("Connection From ", self.client_address)
        connSock = self.request  # 클라이언트와 연결된 소켓
        clientList.append(connSock) # 클라이언트 리스트에 소켓 저장
        while True:
            try:
                msg = connSock.recv(1024).decode("utf-8") # 데이터 수신
                if msg == "":       # 클라이언트가 close()로 접속 종료
                    connSock.close()
                    print("{} 정상 접속 종료".format(self.client_address))
                    clientList.remove(connSock)
                    break

                print("{}으로부터 수신 : {}".format(self.client_address, msg))
                sendAll(msg, connSock)
            except Exception as e:
                # 비정상적인 접속 종료(주로 클라이언트가 프로그램 바로 종료)
                connSock.close()
                print("{} 비정상 접속 종료 = {}".format(
                    self.client_address, e))
                clientList.remove(connSock)
                break


if __name__ == '__main__':
    # ('', PORT) : 현재 실행 프로세스가 동작하는 Host ip를 자동할당해라
    #              9000포트 설정
    # 새로운 클라이언트가 접속할 때마다 스레드를 1개씩 할당하고
    # 해당 스레드가 RequestHandler객체의 handle메서드를 처리하도록 하라
    server = ThreadingTCPServer(('', PORT), RequestHandler)
    print('Server Start ', PORT)
    server.serve_forever()    # 서버가동시작