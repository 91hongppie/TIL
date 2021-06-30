import sys
sys.stdin = open('BOJ_1174_줄어드는숫자.txt', 'r')

N = int(input())
decreaseNumList = []
count = 0
while True:
    NumList = []
    for i in range(10):
        if len(decreaseNumList) == 0:
            NumList.append(str(i))
            count += 1
            if count == N:
                break
        else:
            for j in decreaseNumList[-1]:
                if i > int(j[0]):
                    NumList.append(str(i)+j)
                    count += 1
                    if count == N:
                        break
                else:
                    break
        if count == N:
            break
    decreaseNumList.append(NumList)
    if len(NumList) == 0:
        break
    if count == N:
        break
if len(NumList) == 0:
    print(-1)
else:
    print(decreaseNumList[-1][-1])

