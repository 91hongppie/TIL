with open('quest.txt', 'w') as f: # f 변수 선언 안하고 바로 쓸 수 있다. 사용할 때 f 로 사용
    for i in range(4):
        f.write(f'{i}\n')
