import sys
sys.stdin = open('SWEA_1949_등산로 조성.txt', 'r')
from pprint import pprint

def road(r, c, leng, dep, nums):
    global result
    for u in range(4):
        x1 = r + dx[u]
        y1 = c + dy[u]
        if 0 <= x1 < rc and 0 <= y1 < rc:
            if board[x1][y1] < board[r][c]:
                if visit[x1][y1] == False:
                    visit[x1][y1] = True
                    road(x1, y1, leng+1, dep, nums)
                    visit[x1][y1] = False
            elif board[x1][y1] >= board[r][c]:
                if nums == 1:
                    for y in range(1, dep+1):
                        if board[x1][y1] - y < board[r][c]:
                            if visit[x1][y1] == False:
                                visit[x1][y1] = True
                                board[x1][y1] -= y
                                road(x1, y1, leng+1, dep, nums-1)
                                board[x1][y1] += y
                                visit[x1][y1] = False
    result = max(result, leng)


N = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for tc in range(1, N+1):
    result = 0
    rc, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(rc)]
    visit = [[False] * rc for _ in range(rc)]
    top = 0
    for r in range(rc):
        top = max(top, max(board[r]))
    top_list = []
    for i in range(rc):
        for j in range(rc):
            if board[i][j] == top:
                top_list.append([i, j])
    for g in top_list:
        visit[g[0]][g[1]] = True
        road(g[0], g[1], 1, K, 1)
        visit[g[0]][g[1]] = False
    print('#{} {}'.format(tc, result))