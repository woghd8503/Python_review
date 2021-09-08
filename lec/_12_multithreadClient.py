from socket import *
import threading

isRun = True
serverIP = "127.0.0.1"
PORT = 9000

def recvData(clientSock):
    try:
        while isRun:
            s = clientSock.recv(1024).decode("utf-8")
            print("<< ", s)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect((serverIP, PORT))

    # 1) main Thread : 입력 후 서버로 전송
    # 2) recv Thread : 서버로부터의 수신 후 화면에 표시

    recvThread = threading.Thread(target=recvData,
                                  args=(clientSock,))
    recvThread.daemon = True # main스레드 종료시 함께 종료
    recvThread.start()

    # main Thread의 역할
    while True:
        s = input(">> ")
        if s == "<stop>":
            isRun = False
            break
        clientSock.send(s.encode())

    clientSock.close()

