import time

def readBook():
    for i in range(10):
        print("책을 읽는다 " + str(i))
        time.sleep(1)

def playMusic():
    for i in range(10):
        print("음악을 즐긴다 " + str(i))
        time.sleep(1)

if __name__ == '__main__':
    readBook()
    playMusic()