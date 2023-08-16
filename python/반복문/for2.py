a = [10, 20, 30, 40, 55]

for i in a:
    if i % 10 == 0:
        print(i)
    else:
        print(i,"는 10의 배수가 아닙니다.")

b = ["a", "b", "c", "d", "e"]

# 리스트 2개를 동시에 반복문으로 접근하기
for i, j in zip(a, b):
    print(i)
    print(j)
    print(i,":",j)