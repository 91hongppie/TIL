import requests
from bs4 import BeautifulSoup
url = 'https://www.naver.com/' #url을 빼서하면 더 좋다.
html = requests.get(url).text #.text 없으면 응답신호만 .text 정보 가져오기
soup = BeautifulSoup(html, 'html.parser') # html 정제하기 str -> bs4.BeautifulSoup로 타입 변경
search = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k') #검색어 순위 리스트에서는 .text 없고 select_one이 아니라 select
print(type(search)) # search의 type확인
for i in search:
    print(i.text)


#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child(1) > a > span
#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child(2) > a > span
#content > div > div.keyword_carousel > div > div > div:nth-child(1) > div > div > ul > li:nth-child(3) > a > span