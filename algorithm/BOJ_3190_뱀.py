import sys
sys.stdin = open('BOJ_3190_뱀.txt', 'r')

N = int(input())
rotateList = [0 for _ in range(10001)]
board = [[0 for _ in range(N)] for _ in range(N)]
appleNum = int(input())
for _ in range(appleNum):
    x, y = list(map(int, input().split()))
    board[x-1][y-1] = 1
timer = int(input())
for _ in range(timer):
    sec, direct = list(map(str, input().split()))
    rotateList[int(sec)] = direct
count = 0
nowdir = 0
dir_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
snake = [[0, 0]]
r, c = [0, 0]
while True:
    if rotateList[count] != 0:
        if rotateList[count] == 'D':
            if nowdir < len(dir_list) - 1:
                nowdir += 1
            elif nowdir  == len(dir_list) -  1:
                nowdir = 0
        elif rotateList[count] == 'L':
            if nowdir > 0:
                nowdir -= 1
            elif nowdir == 0:
                nowdir = len(dir_list) - 1
    r += dir_list[nowdir][0]
    c += dir_list[nowdir][1]
    if [r, c] in snake:
        count += 1
        break
    if 0 <= r < N and 0 <= c < N:
        if board[r][c] == 0:
            for i in range(len(snake)-1):
                snake[i][0] = snake[i+1][0]
                snake[i][1] = snake[i+1][1]
            snake[-1][0] = r
            snake[-1][1] = c
        else:
            board[r][c] -= 1
            snake.append([r, c])
    else:
        count += 1
        break
    count += 1

print(count)
