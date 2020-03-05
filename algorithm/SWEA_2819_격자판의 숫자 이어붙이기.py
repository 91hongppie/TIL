import sys
sys.stdin = open('SWEA_2819_격자판의 숫자 이어붙이기.txt', 'r')

def DFS(r, c, re):
    if len(re) == 7:
        result_set.add(re)
        return
    for k in range(4):
        x1 = r + dx[k]
        y1 = c + dy[k]
        if 0 <= x1 < 4 and 0 <= y1 < 4:
            DFS(x1, y1, re+board[x1][y1])


N = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1] 
for tc in range(1, N+1):
    board = [list(map(str, input().split())) for _ in range(4)]
    result_set = set()
    sen = []
    for i in range(4):
        for j in range(4):
            DFS(i, j, board[i][j])
    print('#{} {}'.format(tc, len(result_set)))
