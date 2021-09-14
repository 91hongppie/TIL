import sys
sys.stdin = open('BOJ_17070_파이프옮기기1.txt', 'r')

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dirPipe = [[0, 1], [1, 1], [1, 0]]



dp[0][1][0] = 1
for i in range(N):
    for j in range(N):
        for k in range(3):
            x1 = i + dirPipe[k][0]
            y1 = j + dirPipe[k][1]
            if 0 <= x1 < N and 0 <= y1 < N:
                if k == 0 and board[x1][y1] == 0:
                    dp[x1][y1][k] += dp[i][j][k] + dp[i][j][k+1]
                elif k == 1 and board[x1][y1] == 0 and board[i][y1] == 0 and board[x1][j] == 0:
                    dp[x1][y1][k] += sum(dp[i][j])
                elif k == 2 and board[x1][y1] == 0:
                    dp[x1][y1][k] += dp[i][j][k] + dp[i][j][k-1]
print(sum(dp[N-1][N-1]))