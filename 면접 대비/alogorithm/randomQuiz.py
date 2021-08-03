import random

numList = [0 for _ in range(11)]
result = 'false'
for _ in range(10):
    num = random.randrange(1, 11)
    if numList[num] == 0:
        numList[num] += 1
    else:
        result = 'true'

print(numList)
print(result)