import threading
import time

def readBook():
    for i in range(10):
        print("책을 읽는다 " + str(i) + "\n", end="")
        time.sleep(1)

def playMusic():
    for i in range(10):
        print("음악을 즐긴다 " + str(i) + "\n", end="")
        time.sleep(1)

# 아래처럼은 동시에 책을 읽고, 음악을 듣는 것을 병행할 수 없다
# if __name__ == '__time__':
#     readBook()
#     playMusic()

# 아래처럼 1개 함수마다 스레드를 1개 할당해야 동시에 병행 진행할 수 있다
if __name__ == '__main__':
    # 모듈에 스레드 할당을 요청하고, 스레드가 담당할 함수를 지정해주고
    # 스레드의 시작, 대기 등을 제어할 스레드 객체를 리턴받는다
    
    # 총 3개의 스레드가 존재한다
    # 1) 프로그램이 실행되면 무조건 생성되는 main 스레드
    # 2) read 스레드
    # 3) play 스레드
    readThread = threading.Thread(target=readBook)
    playThread = threading.Thread(target=playMusic)

    # main 스레드가 종료되면 따라 종료되겠다
    # (사장님이 퇴근하면 바로 따라 퇴근하겠다)
    readThread.daemon = True
    playThread.daemon = True

    # main 스레드가 종료되는 것과 관계없이 끝까지 수행하겠다
    # (기본값)
    readThread.daemon = False
    playThread.daemon = False

    # 마치 알바생 2명이 각각 맡은 일을 알아서 처리하는 것 처럼 일을 시작한다.
    readThread.start()
    playThread.start()

    # 알바생 2명의 일이 각각 끝나기를 기다린다
    # 누가? 사장님이(main thread가)
    readThread.join()
    playThread.join()
    
    print("모든 스레드 종료")








