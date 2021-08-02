import sys
sys.stdin = open('BOJ_5972_택배배송.txt', 'r')

sys.setrecursionlimit(1000000)
N, M = list(map(int, input().split()))

stack = [[] for _ in range(N+1)]
dis = [-1 for _ in range(N+1)]
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    stack[a].append([b, c])
    stack[b].append([a, c])

def findMinRoad(point, d):
    global dis, stack, M
    if point == M:
        if dis[point] == -1:
            dis[point] = d
        else:
            dis[point] = min(dis[point], d)
        return
    for i in stack[point]:
        if dis[i[0]] == -1 or (dis[i[0]] != -1 and dis[i[0]] > d + i[1]):
            dis[i[0]] = d+i[1]
            findMinRoad(i[0], d+i[1])
   


dis[1] = 0
findMinRoad(1, 0)
print(dis[N])