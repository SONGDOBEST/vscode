# num의 값에 따라 양수, 음수, 0입니다 출력
# num = "17"
# if num > 0:
#     print("양수입니다")
# elif num == 0:
#     print("0 입니다.")
# else:
#     print("음수입니다.")

# 자바의 scanner_ 처럼 실행 후 콘솔에서 숫자를 입력받아
# 홀수, 짝수를 판별하여 출력하는 코드를 작성

number = eval(input("숫자를 입력하세요: ")) #int를 붙이든, input함수를 eval로 감싸든 하나를 해야 변수를 "숫자"로 판별함. 안하면 기본적으로 입력받은 값은 "str" 변수가 됨
print(type(number))
if type(number) == float:
    print("실수입니다.")
else:
    if number == 0:
        print("0 입니다.")
    elif number % 2 == 0:
        print("짝수입니다")
    else:
        print("홀수입니다")


