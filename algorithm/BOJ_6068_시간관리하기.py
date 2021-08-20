import sys
sys.stdin = open('BOJ_6068_시간관리하기.txt', 'r')

N = int(input())

playList = []
for n in range(N):
    playList.append(list(map(int, input().split())))
playList.sort(key = lambda x : x[1], reverse=True)
startNum = playList[0][1]
for idx, value in enumerate(playList):
    if startNum > value[1]:
        startNum = value[1]
    elif startNum < 0 and startNum-value[0] < 0:
        break
    startNum = startNum - value[0]
if startNum >= 0:
    print(startNum)
else:
    print(-1)
