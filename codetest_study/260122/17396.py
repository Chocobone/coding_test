# https://www.acmicpc.net/problem/17396
# 가중치(=시간)을 최소화하는 다익스트라 알고리즘?
# 시야가 있는 곳을 없는 취급(visited=false 등)해서 진행해보기

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
ward = list(map(int, input().split()))

INF = 10e9
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    i, j, time = map(int, input().split())
    graph[i][j] = time
    graph[j][i] = time

# BFS
min_time = 10e9
cant_backdoor = False
visited = [[False] * n for _ in range(n)]

def bfs(now):
    #start[0] = Node, start[1] = time
    start = path.popleft()
    for end in range(n):

        if ward[end] == 1 : 
            visited[start[0]][end] = True
        
        if end == n and graph[start[0]][end] != 0:
            if min_time > start[1]:
                min_time = start[1]
                cant_backdoor = False
        if graph[start[0]][end] != INF and not visited[start[0]][end]:
            start[1] += graph[start[0]][end]
            visited[start[0]][end] = True
            path.append([end, start[1]])


print(0 if cant_backdoor else min_time)