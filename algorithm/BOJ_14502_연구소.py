import sys
sys.stdin = open('BOJ_14502_연구소.txt', 'r')
from pprint import pprint
from collections import deque
from copy import deepcopy


def comb(x, y):
    if len(wall_point) == 3:
        points = wall_point[::]
        wall.append(points)
        return
    for i in range(r):
        for j in range(c):
            if board[i][j] == 0 and visit[i][j] == False:
                visit[i][j] = True
                wall_point.append([i, j])
                comb(i, j)
                wall_point.pop()
                visit[i][j] = False

def virus(r1, c1):
    Q.append([r1, c1])
    while Q:
        rx, cy = Q.popleft()
        for w in range(4):
            x1 = rx + dx[w]
            y1 = cy + dy[w]
            if 0 <= x1 < r and 0 <= y1 < c:
                if board1[x1][y1] == 0:
                    board1[x1][y1] = 2
                    Q.append([x1, y1])

r, c = map(int, input().split())
Q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = [list(map(int, input().split())) for _ in range(r)]
visit = [[False] * c for _ in range(r)]
wall = []
wall_point = []
virus_list = []
for t in range(r):
    for g in range(c):
        if board[t][g] == 2:
            virus_list.append([t, g])
comb(0, 0)
result = 0
for point in wall:
    board1 = deepcopy(board)
    sum_zero = 0
    for k in point:
        board1[k[0]][k[1]] = 1
    for h in virus_list:
        virus(h[0], h[1])
    for idx in board1:
        sum_zero += idx.count(0)
    for k in point:
        board1[k[0]][k[1]] = 0
    result = max(result, sum_zero)
print(result)