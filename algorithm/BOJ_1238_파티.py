import sys
sys.stdin = open('BOJ_1238_파티.txt', 'r')

from collections import deque
N, M, X = list(map(int, input().split()))
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
stack = [[] for _ in range(N+1)]

def BFS(start, end, board, stack):
    Q = deque()
    Q.append([start, 0])
    while Q:
        newStart, dis = Q.popleft()
        if board[start][end] != 0 and dis >= board[start][end]:
            continue
        if board[newStart][end] != 0:
            newStart = end
            dis += board[newStart][end]
        if newStart == end:
            if board[start][end] == 0:
                board[start][end] = dis
            else:
                board[start][end] = min(board[start][end], dis)
        else:
            for i in stack[newStart]:
                Q.append([i[0], dis+i[1]])


for i in range(M):
    start, end, dis = list(map(int, input().split()))
    if start == X:
        board[start][end] = dis
    elif end == X:
        board[start][end] = dis
    stack[start].append([end, dis])
# for i in board:
#     print(i)

for i in range(1, N+1):
    if i == X:
        continue
    if board[i][X] == 0:
        BFS(i, X, board, stack)
    if  board[X][i] == 0:
        BFS(X, i, board, stack)

# print('')
totalDis = [0 for _ in range(N+1)]
for i in range(1, N+1):
    totalDis[i] = board[i][X] + board[X][i]
    # print(board[i])
print(max(totalDis))

