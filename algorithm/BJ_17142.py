import sys 
sys.stdin = open('BJ_17142.txt', 'r')
from pprint import pprint
from copy import deepcopy
from collections import deque


def comb(vi_list, s_num):
    if len(vi_list) == nums:
        vi_list = vi_list[::]
        virus_list.append(vi_list)
    for u in range(s_num+1, len(virus)):
        vi_list.append(u)
        comb(vi_list, u)
        vi_list.pop()

def BFS(points, moroom):
    global Q
    for u in points:
        moroom[virus[u][0]][virus[u][1]] = 0
        Q.append([virus[u][0], virus[u][1], 1])
    while Q:
        x, y, times = Q.popleft()
        if times > ans:
            Q = deque()
            return []
        for l in range(4):
            x1 = x + dx[l]
            y1 = y + dy[l]
            if 0 <= x1 < rc and 0 <= y1 < rc:
                if moroom[x1][y1] == -1:
                    moroom[x1][y1] = times
                    Q.append([x1, y1, times+1])
                if moroom[x1][y1] == '*':
                    check = False
                    for w in range(4):
                        x2 = x1 + dx[w]
                        y2 = y1 + dy[w]
                        if 0 <= x2 < rc and 0 <= y2 < rc:
                            if moroom[x2][y2] == -1:
                                check = True
                    if check == True:
                        moroom[x1][y1] = times
                        Q.append([x1, y1, times+1])
    return moroom

rc, nums = map(int, input().split())
room = []
virus = []
for i in range(rc):
    room.append(list(map(int, input().split())))
    for j in range(rc):
        if room[i][j] == 2:
            virus.append([i, j])
            room[i][j] = '*'
        elif room[i][j] == 1:
            room[i][j] = '-'
        elif room[i][j] == 0:
            room[i][j] = -1
Q = deque()
virus_list = []
mo_list = []
for k in range(len(virus)-(nums-1)):
    mo_list.append(k)
    comb(mo_list, k)
    mo_list.pop()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 1000000
for k in virus_list:
    mo_room = deepcopy(room)
    check_list = BFS(k, mo_room)
    num_clean = 0   
    if check_list:
        result = 0
        for row in range(rc):
            for col in range(rc):
                if check_list[row][col] == -1:
                    num_clean += 1
                if check_list[row][col] != '*' and check_list[row][col] != '-':
                    if check_list[row][col] > result:
                        result = check_list[row][col]
    else:
        continue
    if num_clean == 0:
        ans = min(ans, result)
if ans == 1000000:
    print(-1)
else:
    print(ans)