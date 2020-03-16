import sys
sys.stdin = open('SWEA_2105_디저트 카페.txt', 'r')

def DFS(r, c, dezert, dirt, nums):
    if nums > 1:
        if dirt[nums-2] != 0:
            x1 = r + dx[nums]
            y1 = c + dy[nums]
            if 0 <= x1 < rc and 0 <= y1 < rc:
                if board[x1][y1] not in dezert and visit[x1][y1] == False:
                    visit[x1][y1] = True
                    dirt[]
    else:
        for k in range(nums, 2):
            x1 = r + dx[k]
            y1 = c + dy[k]
            if 0 <= x1 < rc and 0 <= y1 < rc:
                if board[x1][y1] not in dezert and visit[x1][y1] == False:
                    visit[x1][y1] = True
                    dirt[k] += 1
                    DFS(x1, y1, dezert.append(board[x1][y1]), dirt, k)
                    dirt[k] -= 1
                    visit[x1][y1] = False

    

    

N = int(input())
dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]
for tc in range(1, N+1):
    rc = int(input())
    board = [list(map(int, input().split())) for _ in range(rc)]
    visit = [[False] * rc for _ in range(rc)]
    for i in range(rc):
        for j in range(rc):
            if i == 0 and j == 0:
                continue
            elif i == rc-1 and j == rc-1:
                continue
            visit[i][j] = True
            DFS(i, j, [board[i][j]], [0, 0, 0, 0], i)
            visit[i][j] = False