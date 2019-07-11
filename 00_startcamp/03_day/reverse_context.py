#DOCstring
"""
다음과 같은 내용의 파일 quest.txt 가 있다.
0
1
2
3

이 파일의 내용을 다음과 같이 역순으로 reverse_quest.txt 라는 파일로 저장하시오.
3
2
1
0

"""
# 1. 읽고
# 2. 뒤집고
# 3. 작성하고

# with open('quest.txt', 'r') as f:
#     all_text = f.read()
# with open('reverse_context.txt', 'w') as f:
#     text = f.write(f'{all_text[::-1].strip()}\n')
    
with open('quest.txt', 'r') as f:
    lines = f.readlines() #리스트로 받아오기

lines.reverse() #리스트 순서변경
with open('reverse_context.txt', 'w') as f: #저장
    for line in lines:
        f.write('line\n') 

# with open('reverse_quest.txt', 'w') as f:


# all_text_reverse() 모든 문자 자리바꿈
