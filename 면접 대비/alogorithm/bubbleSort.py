numList = [7, 3, 4, 6, 5, 2, 1, 9, 8]

for i in range(len(numList)-1, 0, -1):
    for j in range(i):
        if numList[j] > numList[j+1]:
            temp = numList[j]
            numList[j] = numList[j+1]
            numList[j+1] = temp

print(numList)