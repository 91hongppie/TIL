import sys
sys.stdin = open('SWEA_4008_숫자 만들기.txt', 'r')

N = int(input())
for tc in range(1, N+1):
    nums = int(input())
    operators = list(map(int, input().split()))
    numbers = list(map(str, input().split()))
    