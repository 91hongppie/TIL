# 딕셔너리 만들기 - 1
lunch = {
    '중국집' : '02-123-1234'
}

# 딕셔너리 만들기 - 2
dinner = dict(중국집 = '02', 일식집 = '031')

# 딕셔너리에 내용 추가하기
lunch['분식집'] = '031-123-1234'
print(lunch)

# 딕셔너리 내용 가져오기
idol = {
    'bts' : {
        '지민' : 25,
        'RM' : 24
    }
}

# RM의 나이는?
# .get()
print(idol['bts']['RM'])

# idol.get('bts').get('RM')