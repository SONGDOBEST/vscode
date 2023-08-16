# 매개변수 x, 리턴 x
def hello():
    print("안녕하세요")

# hello 함수 호출
hello()

# 매개변수 X, 리턴 O
def pout():
    value = "안녕하셨나요"
    return value
a = pout()
print(a)

#매개변수 O, 리턴 X
def func(c):
    print(c)

value = "식사하세요"
func(value)

#매개변수 O, 리턴 O
def both(d):
    value = d + "반갑습니다."
    return value

e = "이현우님 "
print(both(e))