import sys
sys.stdin = open('SWEA_5658_보물상자비밀번호.txt', 'r')
from collections import deque

num_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}
N = int(input())
for tc in range(1, N+1):
    nums, K = map(int, input().split())
    num_list = deque(map(str, input()))
    nums_set = set()
    plays = len(num_list)//4
    for _ in range(len(num_list)//4):
        for k in range(0, len(num_list), plays):
            mo = ''
            for y in range(plays):
                mo += num_list[k+y]
            nums_set.add(mo)
        num_list.rotate(1)
    result_list = []
    for u in nums_set:
        result = 0
        for k in range(1, plays+1):
            result += num_dict[u[k-1]] * 16 ** (plays-k)
        result_list.append(result)
    result_list.sort(reverse=True)
    print('#{} {}'.format(tc, result_list[K-1]))