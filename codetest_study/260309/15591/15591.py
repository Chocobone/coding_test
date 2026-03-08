# https://www.acmicpc.net/problem/15591

import sys
input = sys.stdin.readline
import heapq
INF = sys.maxsize
N, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))

for _ in range(Q):
    K, V = map(int, input().split())
    dist = [INF] * (N+1)
    dist[V] = 0

    heap = []
    heapq.heappush(heap, (0, V))

    while heap:
        d, now = heapq.heappop(heap)

        if dist[now] < d: continue
        for i in graph[now]:
            if d+i[1] < dist[i[0]]:
                dist[i[0]] = d+i[1]
                heapq.heappush(heap, (d+i[1], i[0]))
    
    result = 0
    for i in dist:
        if i >= K : result += 1

    print(result)
