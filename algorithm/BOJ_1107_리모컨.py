import sys
sys.stdin = open('BOJ_1107_리모컨.txt', 'r')


channelNum = int(input())
breakNum = int(input())
breakBtnList = list(map(int, input().split()))
if channelNum == 100:
    print(0)
elif len(breakBtnList) == 10:
    print(channelNum - 100)
elif channelNum - 100 < len(str(channelNum)):
    print(channelNum - 100)
else:
    nowChannel = ''
    channelStr = str(channelNum)
    count = 0
    for i in channelStr:
        if int(i) not in breakBtnList:
            nowChannel += i
            count += 1
        else:
            j = 1
            while True:
                btnCount = 0
                if 0 <= abs(int(i)-j) < 10 and abs(int(i) - j) not in breakBtnList:
                    nowChannel += str(abs(int(i) - j))
                    count += 1
                    break
                if 0 <= abs(int(i)+j) < 10 and abs(int(i) + j) not in breakBtnList:
                    nowChannel += str(abs(int(i) + j))
                    count += 1
                    break
                if abs(int(i) + j) == 9 or abs(int(i) - j) == 0:
                    btnCount += 1
                    if btnCount == 2:
                        break
                j += 1
    if channelNum - 100 > count + abs(int(nowChannel) - int(channelStr)):
        print(count + abs(int(nowChannel) - int(channelStr)))
    else:
        print(channelNum - 100)
                    
                    