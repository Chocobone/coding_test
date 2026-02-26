#https://www.acmicpc.net/problem/15971

import sys
from collections import deque
input = sys.stdin.readline

N, R1, R2 = map(int, input().split())

# 인접 리스트로 그래프 초기화 (메모리 최적화)
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
# BFS 탐색 함수
def bfs(start, end):
    queue = deque([(start, 0, 0)])
    visited = [False] * (N + 1)
    visited[start] = True
    
    while queue:
        curr, total_dist, max_edge = queue.popleft()
        if curr == end:
            return total_dist - max_edge
            
        # 인접한 노드 탐색
        for next_node, cost in graph[curr]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, total_dist + cost, max(max_edge, cost)))
                
    return 0

print(bfs(R1, R2))
