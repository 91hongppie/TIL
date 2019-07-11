#딕셔너리 반복문 활용하기

lunch = {
    '중국집' : '02-123-1234',
    '분식집' : '031-123-1234',
    '일식집' : '02-987-1254'
}

# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])

# .items()
for key, value in lunch.items():
    print(key, value)

# value만 가져오기
for value in lunch.values():
    print(value)

# key만 가져오기
for key in lunch.keys():
    print(key)