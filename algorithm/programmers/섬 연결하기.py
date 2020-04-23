from collections import deque
from copy import deepcopy

def BFS(num, leng, island, list_leng):
    global answer
    Q = deque()
    Q.append([num, [num], 0])
    while Q:
        nums, num_list, dis = Q.popleft()
        if len(num_list) == list_leng:
            print(dis)
            answer = min(answer, dis)
            continue
        for n in island[nums]:
            if n[1] not in num_list:
                num_list.append(n[1])
                Q.append([n[1], num_list, dis+n[0]])

n = 4
costs = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
answer = 1e15

island = [[] for _ in range(n)]
visit = [False for _ in range(n)]
for k in costs:
    island[k[0]].append([k[2], k[1]])
    island[k[1]].append([k[2], k[0]])
for u in island:
    u.sort()
for r in range(n):
    BFS(r, 0, island, n)