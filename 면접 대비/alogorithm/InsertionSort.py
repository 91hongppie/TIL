numList = [8, 5, 6, 2, 4]

for i in range(1, len(numList)):
    temp = numList[i]
    for j in range(i-1, -1, -1):
        if numList[j] > temp:
            numList[j+1] = numList[j]
        else:
            numList[j+1] = temp
            break
        if j == 0:
            numList[j] = temp



    print(numList)
print(numList)