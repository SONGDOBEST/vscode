from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from konlpy.tag import Kkma
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt
import pymysql


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def scroll_fun():
    while True:
        # 스크롤 하기 전 높이 
        before_scroll = driver.execute_script("return document.documentElement.scrollHeight")
        # 현재 높이 만큼 스크롤 내리기 
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        time.sleep(2)
        # 스크롤 내린 후 높이 
        after_scroll = driver.execute_script("return document.documentElement.scrollHeight")
        # 스크롤 전, 후 높이 비교 
        if before_scroll == after_scroll:
            break


# 브라우저 - selenium
driver = webdriver.Chrome() # 크롬으로
# 주소 - 옥냥이 유튜브 메인
driver.get("https://www.youtube.com/@rooftopcat_official")

# 무한 스크롤 (모든 정보 다 가져와야 하므로)
scroll_fun()
# 제목 요소 가져오기 
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')


# 제목 저장을 위한 리스트
title_list = []

# 조회수 저장을 위한 리스트
hits_list = []

for title in titles:
    # shorts 영상, youtube 영화, 제목데이터 없는 컨텐츠
    if title.get_attribute("aria-label") and title.text and "YouTube 영화" not in title.get_attribute("aria-label"): # shorts 영상을 걸러내기 위한 조건문 
        # aria-label 속성값 가져오기 
        aria_label = title.get_attribute("aria-label")
        # print(aria_label)
        start_index = aria_label.rfind("조회수")+4
        end_index = aria_label.rfind("회")
        hits = aria_label[start_index:end_index]
        # 조회수 값 범위에 따라 분리
        # 조회수 없는 영상은 0으로, 조회수가 1000 미만인 영상은 , 처리 생략
        # 조회수 1,000 이상 영상
        if "," in hits:
            hits = int(hits.replace(",",""))
        # 조회수 없는 영상
        elif not hits:
            hits = 0
        # 조회수 1,000 미만
        else:
            hits = int(hits)
        
        if title.text not in title_list:
            title_list.append(title.text)
            hits_list.append(hits)

conn = pymysql.connect(
    host='127.0.0.1',
    user='prac',
    password='pass',
    db='pythonuser',
    charset='utf8mb4')

cur = conn.cursor()
sql = "insert into `youtube`(title, hit) values(%s, %s);"
tuple_result = list(zip(title_list, hits_list))
cur.executemany(sql, tuple_result)

conn.commit()

crawling_result = {
    "title": title_list,
    "hits": hits_list
}
result = pd.DataFrame(crawling_result)

# 조회수 순 내림차순 후 csv로 저장
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")


#konlpy 이용 title_list에서 text 추출 후 명사, 형용사 추출
okt = Okt()
word_list=[]
for text in title_list:
    for word, tag in okt.pos(text):
    # if tag in 'Noun': #명사만
    # if tag in 'Adjective': #형용사만
        if tag in ['Noun','Adjective']: #명사 형용사 둘다
            word_list.append(word)

#같은 단어 노출 빈도
word_list_count = Counter(word_list)

# 단어로 이루어진 리스트 생성
words = []
for word, count in word_list_count.most_common(5):
    words.append(word)

# words = [word for word, count in word_list_count.most_common(5)]
# 횟수로 이루어진 리스트 생성 
counts = [count for word, count in word_list_count.most_common(5)]
plt.bar(words, counts)
plt.show()
# 워드클라우드 객체 생성 + 한글은 그대로 사용하면 깨지므로, Font를 적용해야함
wc = WordCloud(font_path='malgun')

# counter로 분석한 데이터를 워드클라우드로 변경
result = wc.generate_from_frequencies(word_list_count)

# matplotlib로 이미지 출력 => 출력을 위해서 뜸. (팝업으로 워드클라우드가 뜸)
plt.axis('off') #x, y축은 필요없으므로 생략 => 기본적으로 matplotlib는 그래프를 위한 것이므로.

# 결과를 이미지로 출력할 준비
plt.imshow(result)

#이미지 출력
plt.show()



# 데이터 확인
# print("제목", title_list)
# print("조회수", hits_list)

