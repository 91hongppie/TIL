import sys
sys.stdin = open('BOJ_1068_트리.txt', 'r')
from collections import deque
N = int(input())
answer = 0
nodes = list(map(int, input().split()))
Q = deque()
nodeTree = {}
rootNode = -1
for idx, node in enumerate(nodes):
    if node == -1:
        rootNode = idx
    else:
        if nodeTree.get(node):
            nodeTree[node].append(idx)
        else:
            nodeTree[node] = [idx]
deleteNode = int(input())
Q.append(deleteNode)
while Q:
    newDeleteNode = Q.popleft()
    if nodeTree.get(newDeleteNode):
        for i in nodeTree[newDeleteNode]:
            Q.append(i)
    nodeTree[newDeleteNode] = []
if rootNode != deleteNode:
    Q.append(rootNode)
    while Q:
        newNode = Q.popleft()
        if nodeTree.get(newNode) and len(nodeTree[newNode]) > 0:
            count = 0
            for i in nodeTree[newNode]:
                if i != deleteNode:
                    count += 1
                    Q.append(i)
            if count == 0:
                answer += 1
        else:
            answer += 1
print(answer)
