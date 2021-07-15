import sys
sys.stdin = open('BOJ_1577_도로의개수.txt', 'r')


dire = [[0, -1], [-1, 0]] # 왼쪽, 위쪽
row, column = list(map(int, input().split()))
board = [[[] for _ in range(column+1)] for _ in range(row+1)]
points = [[0 for _ in range(column+1)] for _ in range(row+1)]
K = int(input())
for i in range(K):
    r1, c1, r2, c2 = list(map(int, input().split()))
    if r1 > r2:
        board[r1][c1].append(1)
    elif r2 > r1:
        board[r2][c2].append(1)
    elif c1 > c2:
        board[r1][c1].append(0)
    elif c2 > c1:
        board[r2][c2].append(0)
points[0][0] = 1
for i in range(row+1):
    for j in range(column+1):
        for idx, d in enumerate(dire):
            if len(board[i][j]) != 0 and idx in board[i][j]:
                continue
            newX, newY = i+d[0], j+d[1]
            if 0 <= newX < row+1 and  0 <= newY < column+1:
                points[i][j] += points[newX][newY]

print(points[row][column])

            

