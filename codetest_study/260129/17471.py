# https://www.acmicpc.net/problem/17471

import sys
from collections import deque
from itertools import combinations

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
pops = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    count = line[0]
    neighbors = line[1:]
    for neighbor in neighbors:
        adj[i].append(neighbor - 1)

min_diff = INF

def is_connected(nodes):
    if not nodes:
        return False
    
    start_node = nodes[0]
    q = deque([start_node])
    visited = {start_node}
    count = 1
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v in nodes and v not in visited:
                visited.add(v)
                q.append(v)
                count += 1
    
    return count == len(nodes)

for i in range(1, (1 << N) - 1):
    district_a = []
    district_b = []
    
    sum_a = 0
    sum_b = 0
    
    for j in range(N):
        if (i >> j) & 1:
            district_a.append(j)
            sum_a += pops[j]
        else:
            district_b.append(j)
            sum_b += pops[j]
    
    if is_connected(district_a) and is_connected(district_b):
        diff = abs(sum_a - sum_b)
        if diff < min_diff:
            min_diff = diff

if min_diff == INF:
    print(-1)
else:
    print(min_diff)