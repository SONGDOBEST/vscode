str_var = "안녕하세요"
print(str_var)
print(str_var[0])
print(str_var[1])
print(str_var[3])
# print(str_var[6]) 
#IndexError: string index out of range (배열은 0부터 시작. str_var은 index 번호 4번까지 존재.)

str_var2 = "반갑습니다"
print(str_var + str_var2)

str_var3 = str_var + str_var2
print(str_var3) #str 끼리의 연산은 문자열 + 문자열의 나열