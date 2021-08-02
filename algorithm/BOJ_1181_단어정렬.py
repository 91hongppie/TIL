import sys
sys.stdin = open('BOJ_1181_단어정렬.txt', 'r')

N = int(input())
words = [set() for _ in range(51)]

for _ in range(N):
    word = str(input())
    words[len(word)].add(word)

for i in words:
    if len(i) > 0:
        # wordList = list(i)
        i.sort()
        for j in wordList:
            print(j)
