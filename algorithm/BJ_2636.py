import sys
sys.stdin = open('BJ_2636.txt', 'r')
from pprint import pprint
sys.setrecursionlimit(10**4)

def cheese(x, y):
    visit[x][y] = True
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < row and 0 <= y1 < col:
            if board[x1][y1] == 0:
                if visit[x1][y1] == False:
                    cheese(x1, y1)
                 

def BFS(r1, c1):
    for j in range(4):
        x1 = r1 + dx[j]
        y1 = c1 + dy[j]
        if 0 <= x1 < row and 0 <= y1 < col:
            if visit[x1][y1] == True:
                board[r1][c1] = 0
                melt_point.append([r1, c1])

row, col = map(int, input().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
board = [list(map(int, input().split())) for _ in range(row)]
times = 0
num = 1
visit = [[False] * col for _ in range(row)]
cheese(0, 0)
melt_point = []
result = 0
for t in range(row):
    result += sum(board[t])

while num:
    times += 1
    for r in range(row):
        for c in range(col):
            if board[r][c] == 1:
                BFS(r, c)
    for u in melt_point:
        cheese(u[0], u[1])
    remain_cheese = 0
    for u in range(row):
        remain_cheese += sum(board[u])
    if remain_cheese == 0:
        num = 0
        break
    result = remain_cheese
print(times)
print(result)