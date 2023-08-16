# range
# 0-10 정수만들기
print(range(10))

#range를 list 형태로 변환하여 출력
print(list(range(10))) #0부터 10개.
print(list(range(11))) #0부터 11개.

print("=================")

a=range(11)
print(a)
print(list(a))

print("=================")

b=list(range(5,10)) #5부터 10 전까지의 정수
#range(x,y) -> x이상 y미만까지의 정수를 범위로 지정. x생략시 0이상 y미만으로 범위가 지정됨
print(b)

print("=================")

c=list(range(0,11,2)) #0부터 간격 2로 10까지의 정수
print(c)

