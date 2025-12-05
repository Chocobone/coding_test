import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
candy_tree = {}
for i in range(1, n+1):
    candy_tree[i] = []

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    candy_tree[u].append(v)
    candy_tree[v].append(u)

# print(candy_tree)
# ------------ graph 만들기 --------------

candy_max = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    queue = deque()
    queue.append(i)
    already_poped = []
    result = 1
    for _ in range(k):
        a = queue.popleft()
        if not visited[a]:
            queue.extend(candy_tree[a])
            visited[a] = True
        result += len(queue)
    if result > candy_max:
        candy_max = result

print(candy_max)

# ------ k-depth BFS 통한 max값 추측 ------