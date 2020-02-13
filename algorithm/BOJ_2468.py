import sys
sys.stdin = open('BOJ_2468.txt', 'r')
from collections import deque

def BFS(r, c):
    Q.append([r, c])
    while Q:
        x, y = Q.popleft()
        for dir in range(4):
            x1 = x + dx[dir]
            y1 = y + dy[dir]
            if 0 <= x1 < rc and 0 <= y1 < rc:
                if visit[x1][y1] == False:
                    visit[x1][y1] = True
                    Q.append([x1, y1])

    


rc = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
board = [list(map(int, input().split())) for _ in range(rc)]
result = 0
Q = deque()
range_num = 0
for k in range(rc):
    range_num = max(range_num, max(board[k]))
for o in range(1, range_num+1):
    visit = [[False] * rc for _ in range(rc)]
    for i in range(rc):
        for j in range(rc):
            if board[i][j] <= o:
                visit[i][j] = True
    num_region = 0
    for x in range(rc):
        for y in range(rc):
            if visit[x][y] == False:
                BFS(x, y)
                num_region += 1
    result = max(result, num_region)
if result == 0:
    print(1)
else:
    print(result)
    

