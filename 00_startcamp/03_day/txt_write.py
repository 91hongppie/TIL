# 변수에 만들고 싶은 파일을 open() 해야 한다.
# open() 할때 r: 읽기  / w : 쓰기(겸 덮어쓰기) / a : 추가
# f = open('ssafy.txt', 'w')
# for i in range(10): 
#     f.write(f'This is line {i+1}.\n') #(f'This is line {i+1}.\n')에서 f 뒤에 r을 붙이면 \가 작동하지 않는다.
# f.close() #닫기

# with 구문 (context manager)
with open('with_ssafy.txt', 'w') as f: # f 변수 선언 안하고 바로 쓸 수 있다. 사용할 때 f 로 사용
    for i in range(10):
        f.write(f'This is line {i+1}.\n')
    
# writelines() : list 를 넣어주면, 요소 하나당 한 줄씩 작성한다.
with open('ssafy.txt', 'w') as f:
    f.writelines(['0\n', '1\n', '2\n', '3\n'])


# 이스케이프 문자
# \n : 개행문자(줄바꿈)
# \t : 탭문자
# \\ : \ 출력
# \' : ' 출력
# \" : " 출력
