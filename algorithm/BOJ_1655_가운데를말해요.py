import sys
sys.stdin = open('BOJ_1655_가운데를말해요.txt', 'r')

N = int(input())
numList = []
for i in range(N):
    num = int(input())
    if len(numList) < 2:
        if len(numList) == 0:
            numList.append(num)
            left = num
        else:
            if numList[0] > num:
                numList = [num] + numList         
            else:
                numList.append(num)
            left, right = numList
    else:
        

