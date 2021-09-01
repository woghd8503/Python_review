# 1) 프로그래밍 언어 실행방식
#     a) 컴파일 방식
#         한번에 바로 메모리에 올라갈 수 있도록 빌드시 기계어로 전환
#         모든 준비가 끝나서 실행만 하면 된다
#         속도가 가장 빠른 방식
#         C, C++,
#     b) 중간코드 (byte code, intermediate language)
#         가상머신(Virtual Machine), 공통언어환경(Common Language Runtime(CLR))
#         sw로 만든 가상의 HW가 존재하는 것
#         가상며신에 최적화된 가상며신 기계어
#         이식성을 위해서 속도를 희생
#         실행시 '가상머신 기계어'-> 'OS 기계어'
#         Java, C#
#     c) 인터프리터 방식
#         코드 자체가 실행파일
#         실행하면 1줄씩 읽어서 기계어로 번역
#         가장 속도가 느린 방식
#         장점은 실행중에도 코드를 고칠 수 있다.(유연함)
#         python, javascript...
#         javascript:Chrome V8엔진, 속도향상
#         python: Glue Language(접착제 언어)
#                 다른 언어와 결합해서 많이 사용한다
#                 tensorflow : C++

# 2) 파이썬 라이브러리
#  ; 미리 자주쓰는 기능을 만들어놓은 것
#    파이썬 코드 자체가 곧 실행파일이자 라이브러리
#    라이브러리
#     a) 모듈 : *.py 파일
#     b) 패키지 : 폴더 구조로 된 py파일들의 집합

# 3) 미리 작성된 코드 사용하기
# import math
#
# print(math.factorial(0))
# print(math.pow(2, 32))
# print(math.log(1000))
# print(math.pi)

# 4) _11_Arith.py 모듈 사용하기 - 1번재 방법
# import _11_Arith
#
# help(_11_Arith)
#
# print(_11_Arith)
#
# print(_11_Arith.add(10, 20, 30, 40, 50))
# print(_11_Arith.sub(10, 20, 30, 40, 50))
# print(_11_Arith.mul(10, 20, 30, 40, 50))
# print(_11_Arith.div(10, 20, 30, 40, 50))

# 5) _11_Arith.py 모듈 사용하기 - 2번째 방법
# from _11_Arith import add, sub
#
#
# print(add(1000, 50, 20, 30))
# print(sub(1000, 50, 20, 30))

# _11_Arith.py 모듈 사용하기 - 3번째 방법
# from _11_Arith import *
#
# print(add(1000, 50, 20, 30, 50))
# print(sub(1000, 50, 20, 30, 50))
# print(mul(1000, 50, 20, 30, 50))
# print(div(1000, 50, 20, 30, 50))