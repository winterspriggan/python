print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*3+1)
print('풍선')
print("나비")
print("ㅋ"*9)
print(5>10)
print(10>5)
print(True)
print(False)
print(not True)
print(not (5>10))

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 "+animal +" 이름은 "+name+"이에요")
print(name+"는 "+str(age)+"살이며 "+hobby+"을 아주 좋아합니다")
print(name+"는 어른일까요? " +str(is_adult))
print(5<=5)
print(3==3)
print(1 !=3)
print(not (1!=3))
print((3>0) and (3<5))
print(abs(-5))
print(pow(4,5))
print(max(4,32))
print(min(4,30,99, 0,-8))
print(round(3.14))

from math import *
print(sqrt(16))

from random import *
print(random()) # 0.0~1.0 임의의 실수 생성
print(random()*10)
print(int(random()*10))

print(randrange(1,46))
print(randint(1,45))

print("오프라인 스터디 모임 날짜는 매월 " +str(randint(4,28))+"일로 정해졌습니다.")

sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고
파이썬은 쉬워요
"""
print(sentence3)