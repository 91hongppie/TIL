# import webbrowser #웹브라우저 가져오기

# # 1. 리스트가 필요
# # address = ['www.google.com', 'www.youtube.com', 'www.naver.com']
# idols = ['bts', 'nrg', 'hot', 'babyvox']
# url = 'https://search.naver.com/search.naver?query='

# # 2. 반복문(for) 안에서 webbrowser.open() 이 실행
# # for idol in idols:
# #     webbrowser.open_new(url + idol)
    



import requests

response = requests.get('https://www.naver.com/').status_code
print(response)





