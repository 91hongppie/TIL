numList = [7, 0, 8, 3, 9, 4, 6, 5, 2, 1]


for i in range(len(numList)-1):
    num = numList[i]
    idx = i
    for j in range(i+1, len(numList)):
        if numList[j] < num:
            num = numList[j]
            idx = j
    if numList[i] == numList[idx]:
        continue
    print(numList)
    temp = numList[i]
    numList[i] = numList[idx]
    numList[idx] = temp
print(numList)