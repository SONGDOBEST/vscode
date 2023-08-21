import pandas as pd

scores = pd.DataFrame(
    [
        [97, 82, 58, 72, 87], # java
        [88, 100, 92, 68, 89], # python
        [82, 77, 87, 91, 81]  # js
    ]
)
print(scores) # 행과 열은 index번호로 구성됨

scores = pd.DataFrame(
    [
        [97, 82, 58, 72, 87], # java
        [88, 100, 92, 68, 89], # python
        [82, 77, 87, 91, 81]  # js
    ],
    index=["java", "python", "js"] #행의 index값 변경
)
print(scores)

student_number = [1, 2, 3, 4, 5, 6]
# scores = pd.DataFrame(
#     [
#         [97, 88, 82],
#         [82, 100, 77],
#         [58, 92, 87],
#         [72, 68, 91],
#         [87, 89, 81],
#     ],
#     index = student_number
# )
# print(scores)

# scores = pd.DataFrame(   #중괄호 대괄호 구분 잘 하기(열 인덱스 변경시 중괄호 사용)
#     {
#         "java": [97, 82, 58, 72, 87], # java
#         "python": [88, 100, 92, 68, 89], # python
#         "js": [82, 77, 87, 91, 81]  # js   각각 list의 같은 인덱스번호의 값들은 같은 열에 삽입됨
#     },
#     index=student_number #행의 index값 변경
# )
# print(scores)

# # # 이름 데이터 추가 (열 추가)
# scores["이름"] = ["이현우", "김범수", "박찬욱", "손흥민", "김철수"]
# print(scores)

# # # 데이터 추가 (행추가)
# scores.loc[6] = [77, 87, 97, "이지수"]
# print(scores) # 한 줄(한 series)을 추가하는 것.

# 학번, 이름, 성적을 모두 포함한 DataFrame 선언
scores = pd.DataFrame(
    {
        "이름": ["이현우", "김범수", "박찬욱", "손흥민", "김철수", "이지수"],
        "java": [97, 82, 58, 72, 87, 77], # java
        "python": [88, 100, 92, 68, 89, 87], # python
        "js": [82, 77, 87, 91, 81, 97]  # js   각각 list의 같은 인덱스번호의 값들은 같은 열에 삽입됨
    },
    index=student_number
)#.transpose() # 행과 열을 바꿈
print(scores)

# index 기준 내림차순 정렬
print(scores.sort_index(ascending=False))
# java 값 기준 내림차순 정렬
print(scores.sort_values(by="java", ascending=False)) #by 라는 매개변수를 사용하여 기준이 되는 열 지정
# 이름 기준 오름차순 정렬
print(scores.sort_values(by="이름"))

# 첫 N줄만 조회 (index번호 기준)
print(scores.head(3))
# 마지막 N줄만 조회후 그 안에서 js점수 기준 내림차순
print(scores.tail(3).sort_values(by="js", ascending=False))


# DataFrame을 csv로 내보내기    csv :: excel보다 더 범용적으로 사용할 수 있는 형식
scores.to_csv("./scores.csv", encoding="utf-8-sig")


#딕셔너리 데이터를 DataFrame으로 전환
# scores_dict = {
#     "java": [97, 82, 58, 72, 87], # java
#     "python": [88, 100, 92, 68, 89], # python
#     "js": [82, 77, 87, 91, 81]  # js   각각 list의 같은 인덱스번호의 값들은 같은 열에 삽입됨
# }
# scores = pd.DataFrame(scores_dict) # dictionary(key와 value)와 pandas의 Dataframe과 형식 유사함.
# print(scores)

