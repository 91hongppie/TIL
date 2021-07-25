import sys
sys.stdin = open('BOJ_2253_점프.txt', 'r')

from collections import deque
N, M = list(map(int, input().split()))
check = [True for _ in range(N+1)]
steps = [0 for _ in range(N+1)]
result = -1
for _ in range(M):
    num = int(input())
    check[num] = False
def crossBridge(num, dis, count):
    global N, result
    Q = deque()
    Q.append([num, dis, count])
    while Q:
        newNum, newDis, newCount = Q.popleft()
        if steps[newNum] == 0:
            steps[newNum] = newCount
        else:
            if steps[newNum] < newCount:
                continue
        if newNum+newDis+1 <= N and check[newNum+newDis+1] == True:
            if newNum+newDis+1 == N:
                result = newCount+1
                return
            Q.append([newNum+newDis+1, newDis+1, newCount+1])
        if newNum+newDis <= N and check[newNum+newDis] == True:
            if newNum+newDis == N:
                result = newCount + 1
                return
            Q.append([newNum+newDis, newDis, newCount+1])
        if newDis > 1 and newNum+newDis-1 <= N and check[newNum+newDis-1] == True:
            if newNum+newDis -1 == N:
                result = newCount + 1
                return
            Q.append([newNum+newDis-1, newDis-1, newCount+1])

crossBridge(1, 1, 0)
print(result)