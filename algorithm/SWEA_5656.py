import sys
sys.stdin = open('SWEA_5656.txt', 'r')
from pprint import pprint
from collections import deque

def findpoint(board, nums):
    points = []
    
    for w in range(W):
        for h in range(H):
            if mo_board[h][w] != 0:
                points.append([h, w])
                break
    return points

def DFS(r, c, nums):
    if mo_board[x][y] == 1:
        mo_board[x][y] = 0
    elif mo_board[x][y] > 1:
        for k in range(4):
            for u in range(mo_board[x][y]):
                x1 = x + dx[k] * u
                y1 = y + dy[k] * u
                if 0 <= x1 < H and 0 <= y1 < W:
                    DFS(x1, y1)
        mo_board[x][y] = 0
    pprint(mo_board)
    clean(mo_board, nums)

def clean(board_list, nums):
    for x in range(W-1, -1, -1):
        for y in range(H-1, 0, -1):
            if board_list[y][x] == 0:
                board_list[y][x], board[y-1][x] = board[y-1][x], board_list[y][x]
    findpoint(board_list, nums)


TC = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for tc in range(1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    point_list = findpoint(board)
    for point in point_list:
        mo_board = board[::]
        n = 0
        DFS(point[0], point[1], n)
