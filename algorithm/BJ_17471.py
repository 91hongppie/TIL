import sys
sys.stdin = open('BJ_17471.txt', 'r')

N = int(input())
points = list(map(int, input().split()))

num = 1
Q = [[] for _ in range(N+1)]

for _ in range(N):
    a = list(map(int, input().split()))
    for i in range(1, len(a)):
        Q[num].append(a[i])
    num += 1

