from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

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


# 브라우저 실행
driver = webdriver.Chrome()
# 유튜브 인급동 페이지 접속
driver.get("https://www.youtube.com/results?search_query=%EC%98%A5%EB%83%A5%EC%9D%B4+ai+%EC%9B%94%EB%93%9C%EC%BB%B5")
time.sleep(2)

# 무한 스크롤 함수 호출
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
        #print("제목", title.text)
        #print("조회수", hits)
        # 제목, 조회수를 각각 리스트에 담기
        # append(): 리스트에 데이터 추가

crawling_result = {
    "title": title_list,
    "hits": hits_list
}

result = pd.DataFrame(crawling_result)
# result.to_csv("./result.csv", encoding="utf-8-sig")

# 조회수 순 내림차순 후 csv로 저장
result.sort_values(by=["hits"], ascending=False).to_csv("./result.csv", encoding="utf-8-sig")

#리스트의 데이터 확인
#print("제목 리스트", title_list)
#print("조회수 리스트", hits_list)
