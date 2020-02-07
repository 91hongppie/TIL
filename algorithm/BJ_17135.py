import sys
sys.stdin = open('BJ_17135.txt', 'r')
from pprint import pprint
from collections import deque
from copy import deepcopy

def comb(num, nums):
    if num > c:
        return
    if len(nums) == 3:
        nums = nums[::]
        comb_list.append(nums)
        return nums
    nums.append(num)
    comb(num+1, nums)
    nums.pop()
    comb(num+1, nums)

def war(archers, count, pan):
    global result
    for _ in range(r):
        enemy_list = set()
        for archer in archers:
            find(archer, dis, enemy_list)
        for k in enemy_list:
            row, col = k
            if pan[row][col] == 0:
                continue
            pan[row][col] = 0
            count += 1
        pan.pop()
        pan.appendleft([0 for _ in range(c)])
    # pprint(pan)
    if count > result:
        result = count

def find(ar, dis, enemy):
    global Q
    Q.append([r, ar, dis])
    while Q:
        x, y, distance = Q.popleft()
        for u in range(3):
            x1 = x + dx[u]
            y1 = y + dy[u]
            if distance > 0:
                if 0 <= x1 < r and 0 <= y1 < c:
                    if visit[x1][y1] == 0:
                        Q.append([x1, y1, distance-1])
                    else:
                        enemy.add((x1, y1))
                        Q = deque()
                        return

            

r, c, dis = map(int, input().split())
dx = [0, -1, 0]
dy = [-1, 0, 1]
board = deque()
Q = deque()
for _ in range(r):
    board.append(list(map(int, input().split())))

comb_list = []
result = 0
num_list = []
comb(0, num_list)
result = 0
for u in comb_list:
    visit = deepcopy(board)
    war(u, 0, visit)
print(result)