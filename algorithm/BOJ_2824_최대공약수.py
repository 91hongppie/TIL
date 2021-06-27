import sys
sys.stdin = open('BOJ_2824_최대공약수.txt', 'r')

N = int(input())
NList = list(map(int, input().split()))
M = int(input())
MList = list(map(int, input().split()))
NDict = {}
MDict = {}
