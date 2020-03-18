import sys
sys.stdin = open('BOJ_16234_인구이동.txt', 'r')
from pprint import pprint
from collections import deque

def check(r, c, nums):
    Q.append([r, c])
    xy_list = []
    while Q:
        x, y = Q.popleft()
        for j in range(4):
            r1 = x + dx[j]
            c1 = y + dy[j]
            if 0 <= r1 < N and 0 <= c1 < N:
                if visit[r1][c1] == 0:
                    if L <= abs(board[x][y] - board[r1][c1]) <= R:
                        visit[r1][c1] = nums
                        xy_list.append([r1, c1])
                        Q.append([r1, c1])
    if len(xy_list) > 0:
        rc_list.append(xy_list)
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
Q = deque()
n = 0
while 1:
    rc_list = []
    visit = [[0] * N for _ in range(N)]
    num = 1
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                check(i, j, num)
                num += 1
    if len(rc_list) == 0:
        break
    for l in rc_list:
        sum_result = 0
        divide = 0
        for u in l:
            sum_result += board[u[0]][u[1]]
            divide += 1
        ans = int(sum_result/divide)
        for u in l:
            board[u[0]][u[1]] = ans
            visit[u[0]][u[1]] = 0
    n += 1
print(n)

    