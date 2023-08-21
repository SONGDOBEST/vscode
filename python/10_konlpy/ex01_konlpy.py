from konlpy.tag import Kkma
from konlpy.tag import Okt
from collections import Counter

# Kkma 모듈 객체 선언
Kkma = Kkma()

print(Kkma.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
print(Kkma.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
print(Kkma.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))

okt = Okt()
print(okt.morphs(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
print(okt.nouns(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))
print(okt.pos(u'안녕하세요 반갑습니다. 파이썬으로 크롤링하기'))


print(okt.normalize(u'안녕하세욬ㅋㅋㅋㅋㅋㅋ'))

text = "안녕하세요. 파이썬입니다. 저는 파이썬을 배우고 있습니다. 파이썬은 너무나 재미있습니다."
# 단어와 종류를 분리
for word, tag in Kkma.pos(text):
    print(word,tag)
for word, tag in okt.pos(text):
    print(word,tag)

word_list=[]
# 명사 ,형용사만 따로 출력 
for word, tag in okt.pos(text):
    # if tag in 'Noun': #명사만
    # if tag in 'Adjective': #형용사만
    if tag in ['Noun','Adjective']: #명사 형용사 둘다
        print(word,tag)
        word_list.append(word)
print(word_list)

# Counter로 text 문장 횟수 출력
print(Counter(text)) # String은 각각이 모두 index에 들어가있으므로 쪼개서 횟수를 셈

text_list = ['파랑', '빨강', '노랑', '빨강', '파랑', '초록', '빨강']
print(Counter(text_list)) # List는 값 전체에 하나의 index값이 부여되어있으므로, 쪼개지 않고 데이터 단위로 횟수를 셈

# 형태소 분석 결과를 Counter로 세어보기
print(Counter(word_list))