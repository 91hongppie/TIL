import sys
sys.stdin = open('BOJ_2573.txt', 'r')
from collections import deque

def BFS(r, c):
    return 

r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
visit = [[False] * c for _ in range(r)]
island_list = []
times = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(1, r-1):
    times = max(times, max(board[i]))
    for j in range(1, c-1):
        if board[i][j] != 0:
            island_list.append([i, j])
        else:
            visit[i][j] = True
for k in range(times):
    n = 0
    for u in range(len(island_list)):
        for k in range(4):
            if board[island_list[u][0]][island_list[u][1]] == 0:
                visit[island_list[u][0]][island_list[u][1]] = True
                island_visit = [False] * len(island_list)
                for b in range(len(island_list)):
                    if board[island_list[b][0]][island_list[b][1]] > 0:
                        BFS(island_list[b][0], island_list[b][1])


                        
                break
            x1 = island_list[u][0] + dx[k]
            y1 = island_list[u][1] + dy[k]
            if 0 <= x1 < r and 0 <= y1 < c:
                if board[x1][y1] == 0:
                    board[island_list[u][0]][island_list[u][1]] -= 1

