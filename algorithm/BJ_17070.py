import sys
sys.stdin = open('BJ_17070.txt', 'r')

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
