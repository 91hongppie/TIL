import sys
sys.stdin = open('BOJ_1323_숫자연결하기.txt', 'r')

toNum, fromNum = list(map(int, input().split()))
remainderList = []
result = 1
newToNum = toNum
toNumLength = len(str(toNum))
while True:
    remainder = newToNum % fromNum
    if remainder != 0:
        if remainder not in remainderList:
            remainderList.append(remainder)
                
            newToNum = toNum * (10**toNumLength) + remainder
            result += 1
            toNumLength += len(str(toNum))
            if result == 100:
                break
        else:
            result = -1
            break
    else:
        break
print(remainderList)
print(result)

