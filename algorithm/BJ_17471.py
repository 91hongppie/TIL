import sys
sys.stdin = open('BJ_17471.txt', 'r')

def comb(nums, nums_list):
    global comb_list
    if len(nums_list) <= N//2:
        a = nums_list[::]
        if a not in comb_list and len(a) > 0:
            comb_list.append(a)
    else:
        return
    if nums < N:
        nums_list.append(nums+1)
        comb(nums+1, nums_list)
        nums_list.pop()
        comb(nums+1, nums_list)

def DFS(num_list, leng):
    global count
    if len(num_list) == leng:
        count += leng
        return
    for k in range(len(num_list)):
        for u in range(len(num_list)):
            if num_list[u] in Q[num_list[k]]:
                if not visit[num_list[u]]:
                    visit[num_list[u]] = True
                    DFS(num_list, leng+1)
            

N = int(input())
points = list(map(int, input().split()))
result = 100000000000
num = 1
Q = [[] for _ in range(N+1)]
num_list = [x for x in range(1, N+1)]
for _ in range(N):
    a = list(map(int, input().split()))
    for i in range(1, len(a)):
        Q[num].append(a[i])
    num += 1
comb_list = []
a_list = []
for k in range(1, N+1):
    a_list.append(k)
    comb(k, a_list)
    a_list.pop()
    comb(k, a_list)

for u in comb_list:
    b_list = []
    visit = [False for _ in range(N+1)]
    for i in num_list:
        if i not in u:
            b_list.append(i)
    count = 0
    visit[u[0]] = True
    DFS(u, 1)
    visit[b_list[0]] = True
    DFS(b_list, 1)
    if count == N:
        sum_u = 0
        sum_b = 0
        for k in u:
            sum_u += points[k-1]
        for y in b_list:
            sum_b += points[y-1]
        result = min(result, abs(sum_u-sum_b))
if result != 100000000000:
    print(result)
else:
    print(-1)
