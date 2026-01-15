# https://www.acmicpc.net/problem/15681
# defaultdict 활용한 tree 생성 및 검증?

import sys
from collections import defaultdict
input = sys.stdin.readline

N, R, Q = map(int, input().split())
tree = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
#parent는 set()
def makeTree(currentNode, parent):
    for node in tree[currentNode]:
        if not node in parent:
            tree[currentNode].append(node)
            makeTree(node, parent.append(currentNode))

# size = [0] * (N+1)
# def countSubTreeNodes(currentNode):
#     size[currentNode] = 1
#     for node in tree[currentNode]:
#         countSubTreeNodes(node)
#         size[currentNode] += size[node]

makeTree(R, {R})
# countSubTreeNodes(R)

print(tree)
print(tree)
# print(size)

# for _ in range(Q):
#     U = int(input())
#     print(size[U])