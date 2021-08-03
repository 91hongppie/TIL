def mergeSort(left, right):
    mid = (left+right) // 2
    if left < right:
        mergeSort(left, mid)
        mergeSort(mid+1, right)
        merge(left, mid, right)

def merge(left, mid, right):
    sortedList = []
    leftStop = mid+1 
    tempLeft = left
    while tempLeft < leftStop and mid+1 < right+1:
        if numList[tempLeft] < numList[mid+1]:
            sortedList.append(numList[tempLeft])
            tempLeft += 1
        elif numList[mid+1] < numList[tempLeft]:
            sortedList.append(numList[mid+1])
            mid += 1
        else:
            sortedList.append(numList[tempLeft])
            sortedList.append(numList[mid+1])
            mid += 1
            tempLeft += 1
    if tempLeft < leftStop:
        for i in range(tempLeft, leftStop):
            sortedList.append(numList[i])
    elif mid+1 < right+1:
        for i in range(mid+1, right+1):
            sortedList.append(numList[i])
    j = 0
    for i in range(left, right+1):
        numList[i] = sortedList[j]
        j += 1
    



numList = [7, 0, 8, 3, 9, 4, 6, 5, 2, 1]
mergeSort(0, len(numList)-1)
print(numList)