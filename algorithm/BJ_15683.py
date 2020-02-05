import sys
sys.stdin = open('BJ_15683.txt', 'r')
from pprint import pprint

def DFS(cctv_num, count):
    if cctv_num == len(cctv_list) - 1:
        return

    u, k = cctv_list[cctv_num][0], cctv_list[cctv_num][1]
    cc_list = [[], [], [], []]
    for i in range(4):
        if i == 0:
            dx, dy = u, k
            while 0 <= dx < r and 0 <= dy < c:
                if 0 <= dx < r and 0 <= dy+1 < c:
                    if board[dx][dy+1] != 6:
                        if board[dx][dy+1] == 0:
                            cc_list[i].append([dx, dy+1])
                    else:
                        break
                dy += 1
        elif i == 1:
            dx, dy = u, k
            while 0 <= dx < r and 0 <= dy < c:
                if 0 <= dx+1 < r and 0 <= dy < c:
                    if board[dx+1][dy] != 6:
                        if board[dx+1][dy] == 0:
                            cc_list[i].append([dx+1, dy])
                    else:
                        break
                dx += 1
        elif i == 2:
            dx, dy = u, k
            while 0 <= dx < r and 0 <= dy < c:
                if 0 <= dx < r and 0 <= dy-1 < c:
                    if board[dx][dy-1] != 6:
                        if board[dx][dy-1] == 0:
                            cc_list[i].append([dx, dy-1])
                    else:
                        break
                dy -= 1
        elif i == 3:
            dx, dy = u, k
            while 0 <= dx < r and 0 <= dy < c:
                if 0 <= dx-1 < r and 0 <= dy < c:
                    if board[dx-1][dy] != 6:
                        if board[dx-1][dy] == 0:
                            cc_list[i].append([dx-1, dy])
                    else:
                        break
                dx -= 1
    if cctv_list[cctv_num][2] == 1:
        for y in range(4):
            result = cc_list[y]
            for k in result:
                if board[k[0]][k[1]] == 0:
                    board[k[0]][k[1]] = '#'
            DFS(cctv_num+1, count)
            for k in result:
                if board[k[0]][k[1]] == '#':
                    board[k[0]][k[1]] = 0
        
    elif cctv_list[cctv_num][2] == 2:
        for y in range(2):
            result = cc_list[y] + cc_list[y+2]
            for k in result:
                if board[k[0]][k[1]] == 0:
                    board[k[0]][k[1]] = '#'
            DFS(cctv_num+1, count)
            for k in result:
                if board[k[0]][k[1]] == '#':
                    board[k[0]][k[1]] = 0
    elif cctv_list[cctv_num][2] == 3:
        for y in range(-1, 3):
            result = cc_list[y] + cc_list[y+1]
            for k in result:
                if board[k[0]][k[1]] == 0:
                    board[k[0]][k[1]] = '#'
            DFS(cctv_num+1, count)
            for k in result:
                if board[k[0]][k[1]] == '#':
                    board[k[0]][k[1]] = 0
    elif cctv_list[cctv_num][2] == 4:
        for y in range(-1, 2):
            result = cc_list[y] + cc_list[y+1] + cc_list[y+2]
            for k in result:
                if board[k[0]][k[1]] == 0:
                    board[k[0]][k[1]] = '#'
            DFS(cctv_num+1, count)
            for k in result:
                if board[k[0]][k[1]] == '#':
                    board[k[0]][k[1]] = 0
    elif cctv_list[cctv_num][2] == 5:
        result = cc_list[0] + cc_list[1] + cc_list[2] + cc_list[3]
        for k in result:
            if board[k[0]][k[1]] == 0:
                board[k[0]][k[1]] = '#'
        DFS(cctv_num+1, count)
        for k in result:
            if board[k[0]][k[1]] == '#':
                board[k[0]][k[1]] = 0


# 1. 한쪽, 2. 양옆, 3. 위 오른쪽, 4. 위 양옆, 5. 사방
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
r, c = map(int, input().split())
result_num = 1000000
board = []
cctv_list = []
for _ in range(r):
    board.append(list(map(int, input().split())))
for row in range(r):
    for col in range(c):
        if board[row][col] != 0 and board[row][col] != 6:
            cctv_list.append([row, col, board[row][col]])
cctv_list.sort(key=lambda board: board[2], reverse=True)
DFS(0, 0)
count = 0
for x in range(r):
    for y in range(c):
        if board[x][y] == 0:
            count += 1
pprint(board)
print(count)
