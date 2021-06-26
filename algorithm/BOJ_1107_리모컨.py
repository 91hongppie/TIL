import sys
sys.stdin = open('BOJ_1107_리모컨.txt', 'r')

def findChannel(strNum, count, newResult):
    global result
    for i in notBreakNum:
        newCount = count + 1 + abs(int(strNum+str(i)) - channelNum)
        if newResult > newCount:
            findChannel(strNum+str(i), count+1, newCount)
        else:
            result = min(result, newResult)
            return




channelNum = int(input())
breakNum = int(input())
if breakNum != 0:
    breakBtnList = list(map(int, input().split()))
else:
    breakBtnList = []
result = 1e9
notBreakNum = []
for i in range(10):
    if i not in breakBtnList:
        notBreakNum.append(i)
for j in notBreakNum:
    findChannel(str(j), 1, abs(channelNum-j)+1)
print(min(abs(100 - channelNum), result))