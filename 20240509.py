#list

my_list = ['오예스', '몽쉘', '초코파이', '초코파이']
your_list = [1,2,3.14 , True, False , '아무거나']
empty_list = [] #빈 리스트
print(my_list)
print(your_list)
print(empty_list)
print(my_list[0])
print(my_list[0:2])
print('몽쉘'in my_list) #in my list
print(len(my_list)) # 몇 개?
my_list[1] = '몽쉘카카오' #값 수정
print(my_list)
my_list.append('빅파이') #맨 뒤에 값 추가
print(my_list)
my_list.remove('오예스') #값 제거
print(my_list)
my_list.extend(your_list) # 리스트 확장
print(my_list)
my_list.insert(0, '오오예스')
print(my_list)
my_list.pop()
print(my_list)
my_list.clear()
#print(my_list)
my_list.clear()
my_list =  [ 1, 2,3,4]
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.count(1))
print(my_list)
print(my_list.index(2))
my_list.sort()
print(my_list)



#튜플 : 수정 불가한 리스트 , 읽기 전용

my_tuple = ('오예스' , '몽쉘' , '초코파이')
print(my_tuple)
print(my_tuple[0])

#my_tuple[0] = '나나나'  
#print(my_tuple)
print(my_tuple[0:2])

print('몽' in my_tuple) #False
print('몽쉘' in my_tuple) #True

print(len(my_tuple))
print("count:" , my_tuple.count('몽쉘'))
print("index:" ,my_tuple.index('몽쉘'))

(pie1, pie2, pie3) = my_tuple #언패킹
print(pie1, pie2, pie3)

# * Astrick

numbers = (1,2,3,4,5,6,7,8,9,10)
(one, two, *others) = numbers # Astrick를 쓰면 리스트형태 변수로 변환
print(others)
others.append(11)
print(others)
(*others , nine , ten) = numbers
print(others)
print(nine)
(one, *others , ten) = numbers
print(others)

# set : 중복을 허용하지 않는다
A = {'돈가스', '보쌈' , '제육덮밥'}
B = {'짬뽕', '초밥', '제육덮밥'}
print(A.intersection(B)) #교집합
print(A.union(B)) #합집합
print(A.difference(B)) #차집합

# print(A[1]) 
# A[1] = '빅파이' # Set는 수정, 접근이 불가능하다.

A.add('닭갈비')
print(A)
A.remove('제육덮밥')
print(A)

# A.clear()
# print(A)

# del A  # 완전 삭제
# print(A) => Error


B = A.copy()
A.discard('닭갈비')
print(B)
print(A)
print(A.isdisjoint(B)) # 겹치는게 없는지
print(A.issubset(B)) # 하위 셋인지
print(A.issuperset(B)) # 상위 셋인지
A.update(B) # 세트 합치기
print(A)