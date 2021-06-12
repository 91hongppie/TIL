import sys
sys.stdin = open('BOJ_1254_팰린드롬만들기.txt', 'r')

N = str(input())
tempN = N
count = 0
if len(tempN)%2 == 0:
    if tempN[0:int(len(tempN)//2)] == tempN[len(tempN)-1:int(len(tempN)//2)-1:-1]:
        print(len(tempN))
        count += 1
else:
    if tempN[0:int(len(tempN)//2)] == tempN[len(tempN)-1:int(len(tempN)//2): -1]:
        print(len(tempN))
        count += 1
if count == 0:
    for i in range(len(N)):
        tempN = N + N[i::-1]
        if len(tempN)%2 == 0:
            if tempN[0:int(len(tempN)//2)] == tempN[len(tempN)-1:int(len(tempN)//2)-1:-1]:
                print(len(tempN))
                break
        else:
            if tempN[0:int(len(tempN)//2)] == tempN[len(tempN)-1:int(len(tempN)//2): -1]:
                print(len(tempN))
                break