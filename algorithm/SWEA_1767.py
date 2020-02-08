import sys
sys.stdin = open('SWEA_1767.txt', 'r')
from pprint import pprint

def DFS(core, count):
    global result, result_length, length, n
    if core == len(cores):
        for u in range(rc):
            for y in range(rc):
                if [u, y] not in cores and [u, y] not in cores2:
                    if visit[u][y] == True:
                        length += 1
        if count >= result:
            result = count
            if result_length > length:
                result_length = length
        length = 0
        return
    n = 0
    for k in range(4):
        n += 1
        distance(cores[core][0], cores[core][1], k, core+1, count+1)
    if n == 0:
        DFS(core+1, count)

def distance(x, y, num, core, count):
    global length, visit, n
    if x == 0 or x == rc-1 or y == 0 or y == rc-1:
        DFS(core, count)
    x1 = x + dx[num]
    y1 = y + dy[num]
    if 0 <= x1 < rc and 0 <= y1 < rc:
        if visit[x1][y1] == False:
            if board[x1][y1] == 0:
                visit[x1][y1] = True
                distance(x1, y1, num, core, count)
                n-=1
                visit[x1][y1] = False

N = int(input())
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
for tc in range(1, N+1):
    length = 0
    count = 0
    result = 0
    n = 0
    result_length = 100000000
    rc = int(input())
    visit = [[False] * rc for _ in range(rc)]
    board = []
    for _ in range(rc):
        board.append(list(map(int, input().split())))
    cores = []
    cores2 = []
    for r in range(rc):
        for c in range(rc):
            if board[r][c] != 0:
                visit[r][c] = True
                if board[r][c] == 1:
                    if r == 0 or r == rc-1 or c == 0 or c == rc - 1:
                        cores2.append([r, c])
                    else:
                        cores.append([r, c])
    DFS(0, 0)
    print('#{} {}'.format(tc, result_length))
