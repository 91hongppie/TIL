import sys
sys.stdin = open('BOJ_14889_스타트와링크.txt', 'r')

def comb(s_n, nums):
    if len(nums) == int(rc/2):
        comb_list.append(nums[::])
        return
    for j in range(s_n+1, rc):
        nums.append(j)
        comb(j, nums)
        nums.pop()

rc = int(input())
board = [list(map(int, input().split())) for _ in range(rc)]
num_list = []
comb_list = []
result = 1e9
for i in range(rc):
    num_list.append(i)
    comb(i, num_list)
    num_list.pop()
for u in comb_list:
    link_list = []
    for k in range(rc):
        if k not in u:
            link_list.append(k)
    start_sum = 0
    link_sum = 0
    for x in u:
        for y in u:
            start_sum += board[x][y]
    for x1 in link_list:
        for y1 in link_list:
            link_sum += board[x1][y1]
    result = min(result, abs(start_sum-link_sum))
print(result)
