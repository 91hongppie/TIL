import sys
sys.stdin = open('BJ_17135.txt', 'r')

r, c, dis = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(map(int, input().split())))
