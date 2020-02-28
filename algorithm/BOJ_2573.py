import sys
sys.stdin = open('BOJ_2573.txt', 'r')
from pprint import pprint
sys.setrecursionlimit(10**4)
from collections import deque

def BFS(r1, c1):
    global n
    if n == 2:
        return
    Q.append([r1, c1])
    while Q:
        x, y = Q.popleft()
        for lo in range(4):
            x1 = x + dx[lo]
            y1 = y + dy[lo]
            if board[x1][y1] > 0 and visit[x1][y1] == False:
                visit[x1][y1] = True
                Q.append([x1, y1])


def melt(r2, c2):
    melt_vol = 0
    for y in range(4):
        x1 = r2 + dx[y]
        y1 = c2 + dy[y]
        if board[x1][y1] == 0:
            melt_vol += 1
    Q1.add((r2, c2, melt_vol))


r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
year = 0
Q = deque()
while 1:
    year += 1
    Q1 = set()
    nums = 0
    for i in range(1, r-1):
        for j in range(1, c-1):
            if board[i][j] > 0:
                melt(i, j)
    for g in Q1:
        if board[g[0]][g[1]] > g[2]:
            board[g[0]][g[1]] -= g[2]
        else:
            board[g[0]][g[1]] = 0
            nums += 1
    sums = 0
    n = 0
    if nums >= 1:
        visit = [[False] * c for _ in range(r)]
        for l in range(1, r-1):
            sums += sum(board[l])
            for m in range(1, c-1):
                if board[l][m] > 0 and visit[l][m] == False:
                    visit[l][m] = True
                    n += 1
                    BFS(l, m)
                if n == 2:
                    break
            if n == 2:
                break
        if n == 2:
            print(year)
            break
        if sums == 0:
            print(0)
            break



    

