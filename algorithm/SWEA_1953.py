import sys
sys.stdin = open('SWEA_1953.txt', 'r')
from pprint import pprint
from collections import deque
def BFS(r, c):
    Q.append([r, c, times-1])
    while Q:
        x, y, t = Q.popleft()
        for e in direc[board[x][y]]:
            x1 = x + dx[e]
            y1 = y + dy[e]
            if 0 <= x1 < row and 0 <= y1 < col:
                if board[x1][y1] in possible[e] and visit[x1][y1] == False and t > 0:
                    visit[x1][y1] = True
                    Q.append([x1, y1, t-1])


N = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
possible = [[1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5], [1, 2, 5, 6]]
direc = [[], [0, 1, 2, 3], [1, 3], [0, 2], [3, 0], [0, 1], [1, 2], [2, 3]]
for tc in range(1, N+1):
    Q = deque()
    row, col, r_point, c_point, times = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(row)]
    visit = [[False] * col for _ in range(row)]
    visit[r_point][c_point] = True
    BFS(r_point, c_point)
    result = 0 
    for i in range(row):
        sums = visit[i].count(True)    
        result += sums
    print('#{} {}'.format(tc, result))