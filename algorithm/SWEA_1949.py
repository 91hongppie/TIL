import sys
sys.stdin = open('SWEA_1949.txt', 'r')

def DFS(row, col, length, nums):
    global result_length
    for t in range(4):
        x = row + dx[t]
        y = col + dy[t]
        if 0 <= x < rc and 0 <= y < rc:
            if visit[x][y] == False:
                if board[row][col] > board[x][y]:
                    visit[x][y] = True
                    DFS(x, y, length+1, nums)
                    visit[x][y] = False
                elif board[row][col] <= board[x][y]:
                    if nums == 1:
                        for q in range(1, K+1):
                            if board[row][col] > board[x][y] - q:
                                board[x][y] -= q
                                visit[x][y] = True
                                DFS(x, y, length+1, nums-1)
                                visit[x][y] = False
                                board[x][y] += q
    if length > result_length:
        result_length = length

N = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for tc in range(1, N+1):
    rc, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(rc)]
    top_height = 0
    result = 0
    result_length = 0
    top_point = []
    visit = [[False] * rc for _ in range(rc)]
    for i in range(rc):
        top_height = max(top_height, max(board[i]))
    for j in range(rc):
        for k in range(rc):
            if board[j][k] == top_height:
                top_point.append([j, k])
    for u in top_point:
        visit[u[0]][u[1]] = True
        DFS(u[0], u[1], 1, 1)
        visit[u[0]][u[1]] = False
        result = max(result, result_length)
    print('#{} {}'.format(tc, result_length))