
#1) 패키지
# ; 모듈들의 집합

# from cal.arith import *
#
# help(help(add))
# help(help(sub))
# help(help(mul))
# help(help(div))
#
# print(add.fadd(10,20))
# print(sub.fsub(10,20))
# print(mul.fmul(10,20))
# print(div.fdiv(10,20))


from cal.shape import *

help(circle)
help(rectangle)
help(triangle)

print(circle.fcirle(3.4))
print(rectangle.frectangle(3.5, 2.5))
print(triangle.ftriangle(2.5, 2))

from cal.human import *

me = my.cmy("홍길동",24,1000000000000,"AR_VR","3대 1000Kg")
me.intro()
me.happy()
me.study()
me.health()