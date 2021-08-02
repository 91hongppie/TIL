import sys
sys.stdin = open('BOJ_16916_부분문자열.txt', 'r')

S = str(input())
P = str(input())
result = 0
i = 0
fail = [0 for _ in range(len(P))]
j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = fail[j-1]
    if (P[i] == P[j]):
        j += 1
        fail[i] = j

j = 0
for i in range(len(S)):
    while j > 0 and S[i] != P[j]:
        j = fail[j-1]
    if S[i] == P[j]:
        if j == len(P) - 1:
            result = 1
            break
        else:
            j += 1

print(result)