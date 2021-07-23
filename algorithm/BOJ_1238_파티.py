import sys
sys.stdin = open('BOJ_1238_파티.txt', 'r')

from collections import deque


N, M, X = list(map(int, input().split()))

FromX = [[] for _ in range(N+1)]
ToX = [[] for _ in range(N+1)]
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
stack = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, dis = list(map(int, input().split()))
    FromX[end].append([start, dis])
    ToX[start].append([end, dis])
def BFS(toNum, board, disArray, num):
    Q = deque()
    Q.append([toNum, 0])
    if num == 1:
        fromNum = toNum
    while Q:
        if num == 0:
            fromNum, dis = Q.popleft()
        else:
            toNum, dis = Q.popleft()
        
        if board[fromNum][toNum] == 0:
            board[fromNum][toNum] = dis
        else:
            if dis >= board[fromNum][toNum]:
                continue
            else:
                board[fromNum][toNum] = dis
        if num == 0:
            for i in disArray[fromNum]:
                newToNum, newDis = i
                Q.append([newToNum, dis+newDis])
        else:
            for i in disArray[toNum]:
                newToNum, newDis = i
                Q.append([newToNum, dis+newDis])


BFS(X, board, FromX, 0)
BFS(X, board, ToX, 1)
board[X][X] = 0
result = []
for i in range(1, N+1):
    totalDis = board[i][X] + board[X][i]
    result.append(totalDis)
print(max(result))