import os

# 1. 해당 파일들이 있는 위치로 이동
os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\change_filenames') # r은 윈도우에서만 맥에서는 필요없다

# 2. 현재 폴더 안에 모든 파일 이름을 수집
filenames = os.listdir('.') #현재 폴더는 . 뒤로가기는 ..

# 3. 각각의 파일명을 돌면서 수정한다.
# for filename in filenames:
#     os.rename(filename, f'SAMSUNG_{filename}')

# 4. SAMSUNG을 SSAFY로 변환
for filename in filenames:
    os.rename(filename, filename.replace('SAMSUNG_', 'SSAFY_'))