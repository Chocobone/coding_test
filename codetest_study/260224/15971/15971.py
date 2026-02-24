#https://www.acmicpc.net/problem/15971

import sys
input = sys.stdin.readline
from collections import defaultdict
sys.setrecursionlimit(10**6)


N, R1, R2 = map(int, input().split())
graph = defaultdict(lambda: [-1] * (N+1))
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
visited = [0] * (N+1)
max_dist = 0

def dfs(start, end):
    global max_dist
    visited[start] = 1
    if start == end:
        return 0
    for i in range(1, N+1):
        if graph[start][i] != -1 and visited[i] == 0:
            result = dfs(i, end)
            if result != -1:
                max_dist = max(max_dist, graph[start][i])
                return result + graph[start][i]
    return -1

print(dfs(R1, R2) - max_dist)