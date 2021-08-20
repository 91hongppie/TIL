import sys
sys.stdin = open('BOJ_17822_원판돌리기.txt', 'r')

N, M, T = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
for _ in range(T):
    x, d, k = list(map(int, input().split()))
    tempX = x - 1
    while tempX < N:
        if d == 0:
            # 시계 방향으로 회전, 맨 뒤의 값을 앞으로
            board[tempX] = board[tempX][M-k::] + board[tempX][:M-k:]
        elif d == 1:
            # 시계 반대 방향으로 회전, 앞의 값을 뒤로
            board[tempX] = board[tempX][k::] + board[tempX][:k:]
        tempX += x
    sumNum = 0
    count = 0
    sameValueArray = []
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                sumNum += board[i][j]
                count +=1 
                if i == 0:
                    if board[i][j] == board[i+1][j]:
                        sameValueArray.append([i, j])
                        sameValueArray.append([i+1, j])
                    if board[i][j] == board[i][j-1]:
                        sameValueArray.append([i, j])
                        sameValueArray.append([i, j-1])
                    if j+1 < M:
                        if board[i][j] == board[i][j+1]:
                            sameValueArray.append([i, j])
                            sameValueArray.append([i, j+1])
                    else:
                        if board[i][j] == board[i][0]:
                            sameValueArray.append([i, j])
                            sameValueArray.append([i, 0])
                elif i == N-1:
                    if board[i][j] == board[i-1][j]:
                        sameValueArray.append([i, j])
                        sameValueArray.append([i-1, j])
                    if board[i][j] == board[i][j-1]:
                        sameValueArray.append([i, j])
                        sameValueArray.append([i, j-1])
                    if j+1 < M:
                        if board[i][j] == board[i][j+1]:
                            sameValueArray.append([i, j])
                            sameValueArray.append([i, j+1])
                    else:
                        if board[i][j] == board[i][0]:
                            sameValueArray.append([i, j])
                            sameValueArray.append([i, 0])
                else:
                    if board[i][j] == board[i-1][j]:
                        sameValueArray.append([i, j])
                        sameValueArray.append([i-1, j])
                    if board[i][j] == board[i][j-1]:
                        sameValueArray.append([i, j])
                        sameValueArray.append([i, j-1])
                    if board[i][j] == board[i+1][j]:
                        sameValueArray.append([i, j])
                        sameValueArray.append([i+1, j])
                    if j + 1 < M:
                        if board[i][j] == board[i][j+1]:
                            sameValueArray.append([i, j])
                            sameValueArray.append([i, j+1])
                    else :
                        if board[i][j] == board[i][0]:
                            sameValueArray.append([i, j])
                            sameValueArray.append([i, 0])
    if len(sameValueArray) > 0:
        for i in sameValueArray:
            board[i[0]][i[1]] = 0
    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    if board[i][j] > sumNum/count:
                        board[i][j] -= 1
                    elif board[i][j] < sumNum/count:
                        board[i][j] += 1
result = 0
for k in range(N):
    result += sum(board[k])
print(result)