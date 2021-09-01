#프로그램 -> 프로세스

#그로그램 : 실행동작을 저장한 코드(파일)
#프로세스 : 프로그램이 메모리에 로딩되어서 동작되는 상태
# ; 프로세스 당작 시 변수에 저장해 놓은 값들은 프로세스 종료시
#  소멸된다
#  다시 살리고 싶다. -> 파일에 기록해 놓아야 한다.
#  그래서 파일입출력이 나온 것이다.

# 2) 프로세스 : 메모리
#    파일 : 하드디스크
#    연결이 필요하다
#    이 연결을 '스트림'이라고 한다.

# 3) 파일입출력, HW통신, 소켓통신
#    양방향 => 스트림 2개가 필요하다
#             입력스트립, 출력스트림

#4) 스트림 생성/닫기
# f = open('새파일.txt', 'w') # 스트림 연결
# f.close()                  # 스트림 닫기

# 5) 파일에 기록하기
# f = open("새파일.txt", "w", encoding="utf-8")
# for i in range(1, 11):
#     #data = str(i) + "번째 줄입니다.\n"
#     data = "{0}번째 줄입니다\n".format(i)
#     f.write(data)
# f.close()


#6) 파일을 읽어서 보여주기
# f = open("새파일.txt", "r", encoding="utf-8")
# line = f.readline()
# print(line)
# f.close()

#7) 파일을 여러 줄 읽어서 보여주기
# f = open("새파일.txt", "r", encoding="utf-8")
# while True:
#     line= f.readline()
#     if not line:
#         break
#     print(line, end="")
# f.close()

#8) 한번에 여러 줄 읽어서 리스트로 반환
# f = open("새파일.txt", "r", encoding="utf-8")
# lines = f.readlines()
# print(lines)
# for line in lines:
#     print(line, end="")
# f.close()

#9) 한번에 모두 읽어서 문자열로 반환
# f = open("새파일.txt", "r", encoding="utf-8")
# data = f.read()
# print(data)
# f.close()

#10) 파일에 데이터 추가하기
f = open("새파일.txt", "a", encoding="utf-8")
for i in range(11, 21):
    data = "{0}번째 새로 추가했습니다\n".format(i)
    f.write(data)
f.close()

#11) with 구문으로 close 없애기
#with구문이 빠져나갈대 자동으로 f.close()를 호출해준다
with open("새파일.txt", "a", encoding="utf-8") as f:
    for i in range(21, 31):
        data = "{0}번재 새로 추가했습니다.\n".format(i)
        f.write(data)