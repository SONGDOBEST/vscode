# 실행하면 콘솔에서 1 또는 2를 입력받고 1은 세로형 구구단, 2는 가로형 구구단을 각각 출력함
# 구구단은 각각 함수로 정의
def sero(a, b):
    for i in range(a,b+1):
        print(i,"단")
        for j in range(1,10):
            print(i,"X",j,"=",i*j)

def garo(a, b):
    for i in range(a,b+1):
        print(i,"단")
        for j in range(1,10):
            print(i,"X",j,"=",i*j, end="")
        print()

def ask(num):
    a = int(input("몇 단부터 할까요? : "))
    b = int(input("몇 단 까지 할까요? : "))
    if num==1:
        sero(a, b)
    elif num==2:
        garo(a, b)
    
  
    


def choose():
    num = int(input("세로형: 1 입력, 가로형: 2 입력 ::"))
    if num == 1:
        ask(num)
    elif num == 2:
        ask(num)
    else:
        print("잘못 된 입력입니다!")



choose()


# 세로형
# for i in range(a,b+1):
#     print(i,"단")
#     for j in range(1,10):
#         print(i,"X",j,"=",i*j)