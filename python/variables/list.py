#나열형 타입: list, tuple, range

# int list type
a=[1,2,3,4,5]
print(a) #list 내 배열이 그대로 출력됨
print(a[1]) #index번째 배열의 값이 출력됨
print(type(a)) #"a"라는 변수의 타입(list타입)이 출력됨

a[3] = 40 # "a" list의 index "3"번의 값을 40으로 변경
print(a)

# str list
b=["너구리", "오소리", "산골매"]
print(b)
print(b[1])

b[1] = "개구리"
print(b)

# 자료형이 섞인 list

c=[17, 32, "49", "파이썬", 72] #여러 자료형을 한 list에 담을 수 있음
print(c)
print(type(c))
print(type(c[0]))
print(type(c[2]))
print(type(c[3])) #str자료형은 print 시 ''와 같이 나옴
print(c[0]+c[1])

# list 내 list
d=[30, 200, ["점심", "저녁"], 47]
print(d)
print(d[2])
print(d[2][1]) #list "d"안의 index 번호 "2"에 있는 값(배열)의 index 번호 "1"에 있는 값 출력
print(d[3])
