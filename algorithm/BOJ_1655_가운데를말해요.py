import sys
sys.stdin = open('BOJ_1655_가운데를말해요.txt', 'r')

N = int(input())
numList = []
for i in range(N):
    num = int(input())
    numList.append(num)
    numList.sort()
    if len(numList) % 2 == 0:
        print(numList[(len(numList)//2)-1])
    else:
        print(numList[len(numList)//2])
    
print([1] + [1, 2, 3])