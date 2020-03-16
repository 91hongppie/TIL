import sys
sys.stdin = open('BOJ_2589_보물섬.txt', 'r')
from collections import deque

def BFS(r1, c1):
    global result
    Q.append([r1, c1, 0])
    while Q:
        x, y, t = Q.popleft()
        result = max(result, t)
        for k in range(4):
            x1 = x + dx[k]
            y1 = y + dy[k]
            if 0 <= x1 < r and 0 <= y1 < c:
                if board[x1][y1] == 'L' and visit[x1][y1] == False:
                    visit[x1][y1] = True
                    Q.append([x1, y1, t+1])



r, c = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
Q = deque()
result = 0
board = [list(map(str, input())) for _ in range(r)]
for i in range(r):
    len_board = [[0] * c for _ in range(r)]
    for j in range(c):
        visit = [[False] * c for _ in range(r)]
        if board[i][j] == 'L':
            visit[i][j] = True
            BFS(i, j)
print(result)