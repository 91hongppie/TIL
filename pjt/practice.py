import csv
import requests
from decouple import config
from datetime import timedelta, datetime
from pprint import pprint

result = {}
for i in range(1):
    key = config('KEY')
    targetDt = datetime(2019, 7, 13) - timedelta(weeks=i)
    targetDt = targetDt.strftime('%Y%m%d')

    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'
    api_data = requests.get(url).json()
        # pprint(api_data)

        # 주간/주말 박스오피스 데이터 리스트로 가져오기.
    movies = api_data.get('boxOfficeResult').get('weeklyBoxOfficeList')
    # pprint(movies)

        # 영화 대표코드 / 영화명 / 누적관객수

        # 영화정보가 담긴 딕셔너리 영화 대표 코드를 추출

url2 = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={20124079}'
api_data2 = requests.get(url2).json()
movies = api_data2.get('movieInfoResult').get('movieInfo').get('movieNmEn')
pprint(movies)