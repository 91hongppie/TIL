import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/marketindex/').text #.text 없으면 응답신호만 .text 정보 가져오기
soup = BeautifulSoup(html, 'html.parser') # html 정제하기 str -> bs4.BeautifulSoup로 타입 변경
exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text #환율 정보 가져오기 chrome - F12 - Ctrl+Shift+C 
exchange1 = soup.select_one('#exchangeList > li > a.head.jpy > div > span.value').text
print(exchange)
print(exchange1)