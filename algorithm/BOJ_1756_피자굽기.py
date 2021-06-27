import sys
sys.stdin = open('BOJ_1756_피자굽기.txt', 'r')

depths, pizzas = list(map(int, input().split()))
depthList = list(map(int, input().split()))
checkDepth = [False for _ in range(depths)]
pizzaList = list(map(int, input().split()))
answer = 0
for pizzaIdx, pizza in enumerate(pizzaList):
    if checkDepth[0] == True and pizzaIdx < pizzas:
        print(0)
        break
    for depthIdx, depth in enumerate(depthList):
        if pizza > depth:
            answer = depthIdx
            checkDepth[depthIdx-1] = True
            break
        elif checkDepth[depthIdx] == True:
            answer = depthIdx
            checkDepth[depthIdx-1] = True
            break
print(answer)