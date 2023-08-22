# 계산기
# def로 사칙연산 만들기

def plus(a, b):
    i = a+b
    print(a,"+",b,"=",i)
def minus(a,b):
    i = a-b
    print(a,"-",b,"=",i)
def div(a,b):
    i = a/b
    print(a,"/",b,"=",i)
def multi(a, b):
    i = a*b
    print(a,"*",b,"=",i)
def ques():
    int(input("1. 다른계산 2. 종료"))



exe = True

while exe:
    i = 1
    while i == 1: 
        method = int(input("어떤 연산을 할까요? 1. 덧셈 2. 뺄셈 3. 나눗셈 4. 곱셈"))
        a = int(input("숫자를 입력하세요: "))
        b = int(input("숫자를 입력하세요: "))
        
        
        if method == 1:
            plus(a, b)
            ques = int(input("1. 다른계산 2. 종료"))
            if ques == 1:
                i = 1
            if ques == 2:
                i = 2
                exe = False
            
        elif method == 2:
            minus(a, b)
            ques = int(input("1. 다른계산 2. 종료"))
            if ques == 1:
                i = 1
            if ques == 2:
                i = 2
                exe = False
        elif method == 3:
            div(a, b)
            ques = int(input("1. 다른계산 2. 종료"))
            if ques == 1:
                i = 1
            if ques == 2:
                i = 2
                exe = False
        elif method == 4:
            multi(a,b)
            ques = int(input("1. 다른계산 2. 종료"))
            if ques == 1:
                i = 1
            if ques == 2:
                i = 2
                exe = False
        else:
            print("잘못된 입력입니다.")
            ques = int(input("1. 다른계산 2. 종료"))
            if ques == 1:
                i = 1
            if ques == 2:
                i = 2
                exe = False