# 1) 예외처리란?
#   프로그래밍 상에서 의도하지 않은 경우 오류가 발생하는데,
#   이 의도치 않은 오류로부터 안전하게 프로그램을 보호하는데 목적이 있다:

# # 2) 정수 입력
# num = input("당신의 점수를 입력하세요 >> ")
# score = int(num)
# if 90 <= score <= 100:
#     print("A학점")
# elif 80 <= score < 90:
#     print("B학점")
# elif 70 <= score < 80:
#     print("C학점")
# elif 60 <= score < 70:
#     print("D학점")
# else:
#     print("F학점")

#3) 예외처리
# num = input("당신의 점수를 입력하세요 >> ")
# try:    # 처리를 시도하다
#     score = int(num)
# except Exception as e:
#     print(e, "잘 못 입력하셨습니다.")
# else:  # 예외가 발생하지 않음
#     if 90 <= score <= 100:
#         print("A학점")
#     elif 80 <= score < 90:
#         print("B학점")
#     elif 70 <= score < 80:
#         print("C학점")
#     elif 60 <= score < 70:
#         print("D학점")
#     else:
#         print("F학점")

# 4) 예외발생시 다시 입력 유도
score = 0
while True:
    num = input("당신의 점수를 입력하세요 >> ")
    try:  # 처리를 시도하다
        score = int(num)
        break # break가 실해되었다는 것은 구문이 정상 실행되었다는 의미임
    except Exception as e:
        print(e, "잘 못 입력하셨습니다.")

if 90 <= score <= 100:
    print("A학점")
elif 80 <= score < 90:
    print("B학점")
elif 70 <= score < 80:
    print("C학점")
elif 60 <= score < 70:
    print("D학점")
else:
    print("F학점")


# 5) 에외의 종류
# ; 사전에 정의된 여러 예외가 있다.
#   어떤 예외가 발생할 지 예측 할 수 있다면
#   해당 예외를 표현하면 된다.
#;  예외의 종류를 잘 모르면
#   Exception 으로 처리해도 무방하다

# try:
#     pass
# except Exception as e:
#     print(e)

# num0 = int(input("정수 >> "))
# num1 = int(input("정수 >> "))
# result = 0
# try:
#     result = num0/num1
# except ZeroDivisionError as e:
#     print(e, "0으로 나눌 수 없습니다")
# else:
#     print("result=", result)

# try:
#     f = open('foo.txt', 'r')
# except FileNotFoundError as e:
#     print(e, "파일이 없습니다")
# else:
#     data = f.read()
#     print(data)
#     f.close()