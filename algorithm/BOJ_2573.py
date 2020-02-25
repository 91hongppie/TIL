import sys
sys.stdin = open('BOJ_2573.txt', 'r')
from collections import deque

def DFS(r1, c1):
    Q.append([r1, c1])
    while Q:
        x, y = Q.popleft()
        for l in range(4):
            x1 = x + dx[l]
            y1 = y + dy[l]
            if 0 <= x1 < r and 0 <= y1 < c:
                if board[x1][y1] > 0:
                    if island_list.index([x1, y1]):
                        ind = island_list.index([x1, y1])
                        if visit[ind] == False:
                            visit[ind] = True
                            Q.append([x1, y1])


r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
Q = deque()
island_list = []
result = 0
result_num = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(1, r):
    for j in range(1, c):
        if board[i][j] > 0:
            island_list.append([i, j])
            result = max(result, board[i][j])
for ku in range(1, result+1):
    poplist = []
    for u in range(len(island_list)):
        board[island_list[u][0]][island_list[u][1]] -= 1
        if board[island_list[u][0]][island_list[u][1]] == 0:
            poplist.append(u)
    if len(poplist) > 0:
        for e in range(len(poplist)-1, -1, -1):
            island_list.pop(poplist[e])
        visit = [False] * len(island_list)
        visit[0] = True
        DFS(island_list[0][0], island_list[0][1])
        nums = visit.count(False)
        if nums != 0:
            print(ku)
            result_num = 1
            break
if result_num == 0:
    print(0)

    

