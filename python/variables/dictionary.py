#dictionary (매핑형, key/value) => java의 Json
a = {
    "dog" : "갱얼쥐",
    "cat" : "고먐미",
    "tiger" : "큰 줄무늬 고먐미",
    "lion" : "큰 갈기 고먐미"
    
    # "key" : "value"

}
print(a)

print(a["dog"]) #dictionary 내의 속성을 찾아서 출력

a["dog"] = "강아지" #dictionary 내의 key값의 value를 변경

print(a["dog"])

a["cow"] = "젖소" #dictionary 내 값 추가 => key와 value를 둘 다 지정해주기
print(a["cow"])

print(a)