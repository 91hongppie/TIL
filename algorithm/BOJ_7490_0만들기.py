import sys
sys.stdin = open('BOJ_7490_0만들기.txt', 'r')

from collections import deque
N = int(input())

Q = deque()
for count in range(N):
    answer = []
    Q.append([str(1), str(1)])
    num = int(input())
    for i in range(2, num+1):
        for _ in range(len(Q)):
            num, result = Q.popleft()
            Q.append([num + '+' + str(i), result + '+' + str(i)])
            Q.append([num + '-' + str(i), result + '-' + str(i)])
            Q.append([num + str(i), result + ' ' + str(i)])
    while Q:
        num, resultStr = Q.popleft()
        if eval(num) == 0:
            answer.append(resultStr)
    answer.sort()
    for i in answer:
        print(i)
    if count != N-1:
        print()
    
