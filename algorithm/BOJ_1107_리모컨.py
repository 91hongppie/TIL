import sys
sys.stdin = open('BOJ_1107_리모컨.txt', 'r')


def findChannel(fromChannel, toChannel, num):
    global result
    if int(num) not in breakBtnList:
        newFromChannel = fromChannel + num
        calcResult(newFromChannel, toChannel)
        if len(newFromChannel) < len(toChannel):
            findChannel(newFromChannel, toChannel, toChannel[len(newFromChannel)])
    else:
        q = 0
        c = 0
        while True:
            if 0 <= int(num)-q < 10:
                if int(num)-q == 0:
                    c += 1
                if int(num) - q not in breakBtnList:
                    findChannel(fromChannel, toChannel, str(int(num) - q))
            if 0 <= int(num)+q < 10:
                if int(num) + q == 9:
                    c += 1
                if int(num) + q not in breakBtnList:
                    findChannel(fromChannel, toChannel, str(int(num) + q))
            if c == 2:
                break
            q += 1
def calcResult(fromChannel, toChannel):
    global result
    tempCount = len(fromChannel) + abs(int(fromChannel) - int(toChannel))
    result = min(result, tempCount)
    return

channelNum = int(input())
breakNum = int(input())
breakBtnList = list(map(int, input().split()))
if channelNum == 100:
    print(0)
elif len(breakBtnList) == 10:
    print(abs(channelNum - 100))
elif abs(channelNum - 100) < len(str(channelNum)):
    print(abs(channelNum - 100))
else:
    result = abs(channelNum - 100)
    channelStr = str(channelNum)
    findChannel('', channelStr, channelStr[0])
    print(result)