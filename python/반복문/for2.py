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

c = ["이", "강", "현", "아", "우", "지"]
for i in range(0,6,2):
    print(c[i], end="")
for j in range(1,6,2):
    print(c[j], end="")
print()
print("==========================")
d = [[1, "a"], [2, "b"], [3, "c"]]
for i, j in d:
    print(i, j)