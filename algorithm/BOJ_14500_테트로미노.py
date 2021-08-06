import sys
sys.stdin = open('BOJ_14500_테트로미노.txt' ,'r')

N, M = list(map(int, input().split()))
result = 0
board = []
for _ in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
blocks = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],  # 긴거
    [[0, 0], [1, 0], [2, 0], [3, 0]], 
    [[0, 0], [0, 1], [1, 0], [1, 1]],  # 정사각형
    [[0, 0], [1, 0], [2, 0], [2, 1]],   # ㄴ 자
    [[0, 0], [1, 0], [2, 0], [2, -1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [-1, 0], [-2, 0], [-2, 1]],
    [[0, 0], [-1, 0], [-2, 0], [-2, -1]],
    [[0, 0], [0, -1], [0, -2], [1, -2]],
    [[0, 0], [0, -1], [0, -2], [-1, -2]],
    [[0, 0], [1, 0], [1, 1], [2, 1]], # ㄹ자
    [[0, 0], [1, 0], [1, -1], [2, -1]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 1]], # ㅗ자
    [[0, 0], [0, 1], [0, 2], [-1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, -1]]
    ]
for i in range(N):
    for j in range(M):
        for block in blocks:
            sumNum = 0
            for b in block:
                if 0 <= i+b[0] < N and 0 <= j+b[1] < M:
                    sumNum += board[i+b[0]][j+b[1]]
                else:
                    sumNum = 0
                    break
            result = max(result, sumNum)
print(result)
