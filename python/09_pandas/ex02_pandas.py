import pandas as pd

# 성적 다루는 간단한 예제
# 학번 정보
student_number = [101, 102, 103, 104, 105]
score_java = pd.Series([92, 98, 59, 67, 82], index=student_number)
score_python = pd.Series([88, 77, 99, 72, 91], index=student_number)
print(score_java)
print(score_python)

# java, python 시리즈 합계
total = score_java + score_python
print(total)

score_js = pd.Series([77, 82, 87, 91, 85], index=[103,102,105,104,101])
print(score_js) #index 조합은 같으나 순서는 뒤죽박죽

# index 값 기준으로 정렬하여 출력
#print(score_js.sort_index())

# java, python, js 총 합계
total = score_js + score_java + score_python
print(total) # index 따라서 합산이 잘 되어서 출력이 된다. (입력한 순서는 상관이 없고, index가 기준이 되어서 잘 된다)

# index 기준 내림차순 정렬
print(total.sort_index(ascending=False)) #오름차순(ascending이 기본값(true) 상태이기 때문에 ascending 상태를 False로 주어야 한다)
# 값 기준 오름차순 정렬
print(total.sort_values())
print(total.sort_values(ascending=False))