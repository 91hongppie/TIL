import sys
sys.stdin = open('BJ_2667.txt', 'r')
from collections import deque

def BFS(x, y):
    Q.append([x, y])
    n = 1
    while Q:
        r, c = Q.popleft()
        for u in range(4):
            x1 = r + dx[u]
            y1 = c + dy[u]
            if 0 <= x1 < N and 0 <= y1 < N:
                if board[x1][y1] == '1':
                    if visit[x1][y1] == False:
                        visit[x1][y1] = True
                        n += 1
                        Q.append([x1, y1])
    danzi_list.append(n)

N = int(input())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
board = []
Q = deque()
for _ in range(N):
    board.append(list(str(input())))
visit = [[False]*N for _ in range(N)]
result = 0
danzi_list = []
for r in range(N):
    for c in range(N):
        if board[r][c] == '1' and visit[r][c] ==False:
            result += 1
            visit[r][c] = True
            BFS(r, c)
danzi_list.sort()
print(len(danzi_list))
for y in danzi_list:
    print(y)