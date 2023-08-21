import pandas as pd

# 시리즈 선언
series1 = pd.Series([2, 4, 6, 8, 10])
print(series1)

# index 지정
series2 = pd.Series([2, 4, 6, 8, 10], index=[1, 2, 3, 4, 5])
print(series2)

# range로 index 지정
series3 = pd.Series([2, 4, 6, 8, 10], index=range(1,6))
print(series3)

# index용 리스트
index_value = [10, 11, 12, 13, 14]
series4 = pd.Series([2, 4, 6, 8, 10], index=index_value)
print(series4) #index를 사용함에 있어서 굉장히 자유로움

# 데이터, index를 따로 선언 후 활용
data_value = ['이', '현', '우', '학', '생']
index_value2 = [9, 10, 11, 12, 13]
series5 = pd.Series(data_value, index=index_value2)
print(series5)