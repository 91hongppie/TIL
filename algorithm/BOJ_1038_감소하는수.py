N = 1000
numList = [[] for _ in range(10)]
count = -1
i = ''
for u in range(10):
    count += 1
    numList[0].append(str(u))
    if count == N:
        i = numList[0][-1]
        break
if count != N:
    idx = 0
    breaker = True
    while count != N:
        if idx + 1 > len(numList):
            i = -1
            break
        for j in range(10):
            for k in numList[idx]:
                if j > int(k[0]):
                    numList[idx+1].append(str(j)+k)
                    count += 1
                    if count == N:
                        i = numList[idx+1][-1]
                        breaker = False
                        break
                else:
                    break
            if breaker == False:
                break
        idx += 1
print(i)

