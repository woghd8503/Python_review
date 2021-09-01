
def add(*args):
    "더하기"
    num = 0
    for i in args:
        num += i
    return num

def sub(*args):
    "빼기"
    num = args[0]
    for i in range(1, len(args)):
        num -= args[i]
    return num

def mul(*args):
    "곱하기"
    num = 1
    for i in args:
        num *= i
    return num

def div(*args):
    "나누기"
    num = args[0]
    for i in range(1, len(args)):
        num /= args[i]
    return num


if __name__ == '__main__':
    print(__name__, "_11_Arith.py 직접 실행시")
    print(add(10, 20, 30))
    print(sub(10, 20, 30))
    print(mul(10, 20, 30))
    print(div(10, 20, 30))
else:
    print(__name__, " 다른 py 파일에서 import 시")

