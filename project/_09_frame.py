import time

def readBook(i):
    print("책을 읽는다 " + str(i))

def playMusic(i):
    print("음악을 즐긴다 " + str(i))


if __name__ == '__main__':
    for i in range(20):
        if i % 2 == 0:
            readBook(i)
        else:
            playMusic(i)

        time.sleep(1)