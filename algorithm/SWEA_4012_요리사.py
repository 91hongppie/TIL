import sys
sys.stdin = open('SWEA_4012_요리사.txt', 'r')

def comb(num, nums):
    if len(nums) == rc/2:
        num_list.append(nums[::])
        return
    if num == rc:
        return
    nums.append(num)
    comb(num+1, nums)
    nums.pop()
    comb(num+1, nums)


N = int(input())

for tc in range(1, N+1):
    rc = int(input())
    board = [list(map(int, input().split())) for _ in range(rc)]
    visit = [False] * rc
    num_list = []
    comb(0, [])
    bo_list = [i for i in range(rc)]
    result = 1e9
    
    leng = int(len(num_list)/2)
    for u in num_list[:leng:]:
        b_list = []
        for k in bo_list:
            if k not in u:
                b_list.append(k)
        a = 0
        b = 0
        for i in u:
            for j in u:
                a += board[i][j]
        for d in b_list:
            for e in b_list:
                b += board[d][e]
        c = abs(a-b)
        result = min(result, c)
    print('#{} {}'.format(tc, result))
