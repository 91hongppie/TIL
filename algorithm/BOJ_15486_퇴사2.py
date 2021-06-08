import sys
sys.stdin = open('BOJ_15486_퇴사2.txt', 'r')

N = int(sys.stdin.readline())
dayList = [0 for _ in range(N)]
costList =[0 for _ in range(N)]
dp = [0 for _ in range(N+1)]
result = 0
for i in range(N):
    dayList[i], costList[i] = map(int, sys.stdin.readline().split())
    

for i in range(N-1, -1, -1):
    if i + dayList[i] <= N:
        dp[i] = max(costList[i] + dp[i+dayList[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])