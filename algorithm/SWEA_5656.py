import sys
sys.stdin = open('SWEA_5656.txt', 'r')
from pprint import pprint
from collections import deque
from copy import deepcopy


def find(point_list):
    Q = deque()
    mo_board = deepcopy(board)
    for point in point_list:
        for h in range(H):
            if mo_board[h][point] == 1:
                mo_board[h][point] = 0
                break
            elif mo_board[h][point] > 1:
                Q.append([h, point])
                while Q:
                    x, y = Q.popleft()
                    for u in range(4):
                        for k in range(1, mo_board[x][y]):
                            x1 = x + dx[u] * k
                            y1 = y + dy[u] * k
                            if 0 <= x1 < H and 0 <= y1 < W:
                                if mo_board[x1][y1] == 1:
                                    mo_board[x1][y1] = 0
                                elif mo_board[x1][y1] > 1:
                                    Q.append([x1, y1])
                    mo_board[x][y] = 0
                for w in range(W):
                    for h in range(H-1, -1, -1):
                        if mo_board[h][w] == 0:
                            for h1 in range(h-1, -1, -1):
                                if mo_board[h1][w] >= 1:
                                    mo_board[h][w], mo_board[h1][w] = mo_board[h1][w], mo_board[h][w]
                                    break
                break
    sort(mo_board)


def sort(result_list):
    global result
    blocks = 0
    for h in range(H):
        for w in range(W):
            if result_list[h][w] > 0:
                blocks += 1
    result = min(result, blocks)


def choice(choice_list):
    global result
    if result == 0:
        return
    if len(choice_list) == times:
        find(choice_list)
        return
    for w in range(W):
        choice_list.append(w)
        choice(choice_list)
        choice_list.pop()

N = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for tc in range(1, N+1):
    times, W, H = map(int, input().split())
    result = W * H
    board = [list(map(int, input().split())) for _ in range(H)]
    choice([])
    print('#{} {}'.format(tc, result))