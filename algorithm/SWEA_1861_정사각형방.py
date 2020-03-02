import sys
sys.stdin = open('SWEA_1861_정사각형방.txt', 'r')
from pprint import pprint
sys.setrecursionlimit(10**8)

def DFS(r, c):
    global length
    for d in range(4):
        x1 = r + dx[d]
        y1 = c + dy[d]
        if 0 <= x1 < rc and 0 <= y1 < rc:
            if board[x1][y1] == board[r][c] + 1:
                if visit[x1][y1] == 0:
                    DFS(x1, y1)
                else:
                    visit[r][c] = visit[x1][y1] + 1
                    return
    length += 1
    visit[r][c] = length


N = int(input())
for tc in range(1, N+1):
    rc = int(input())
    board = [list(map(int, input().split())) for _  in range(rc)]
    visit = [[0] * rc for _ in range(rc)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(rc):
        for j in range(rc):
            if visit[i][j] == 0:
                length = 0
                DFS(i, j)
    result = 0
    room_number = 1e9
    for u in range(rc):
        result = max(result, max(visit[u]))
    for k in range(rc):
        for y in range(rc):
            if visit[k][y] == result:
                room_number = min(room_number, board[k][y])
    print('#{} {} {}'.format(tc, room_number, result))
