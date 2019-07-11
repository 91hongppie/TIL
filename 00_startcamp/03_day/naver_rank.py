import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'

# 요청 보내서  html 파일 받고
html = requests.get(url).text
# 뷰티풀슾으로 정제
soup = BeautifulSoup(html, 'html.parser')
# select 메서드로 사용해서 list 를 얻어낸다.
rank = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k') # rank까지 보고 싶으면  > span.ah_k 지우기 
with open('example.txt', 'w',encoding= 'utf-8')as f:
        for i in rank:
            f.writelines(f'{i.text}\n')

# 뽑은 list 를 with 구문으로 잘 작성해 보자.(txt)
# with open('example.txt', 'w', encodint= 'utf-8') as f:
#     text = f.writelnes()
