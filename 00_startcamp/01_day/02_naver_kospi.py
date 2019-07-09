import requests #requests 가져오기
from bs4 import BeautifulSoup # bs4 에서 BeautifulSoup 가져오기

# 1. 원하는 주소로 요청을 보내 응답을 저장한다.
html = requests.get('https://finance.naver.com/sise/').text
print(html)
# soup = BeautifulSoup(html, 'html.parser')
# kospi = soup.select_one('#KOSPI_now').text
# print(kospi)