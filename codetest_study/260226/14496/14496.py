#https://www.acmicpc.net/problem/14496

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

first, last = map(int, input().split())
N, M = map(int, input().split())

graph = defaultdict(list)
visited = [False] * (N + 1)

# 양방향 그래프 구성
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start, end):
    # 시작점과 도착점이 이미 같은 경우
    if start == end:
        return 0
    # 큐에는 (현재 노드, 현재까지의 치환 횟수)를 튜플로 담습니다.
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        current, dist = queue.popleft()
        # 목적지에 도달한 경우 현재까지의 거리 반환
        if current == end:
            return dist
            
        # 인접 노드 탐색
        for nxt in graph[current]:
            if not visited[nxt]:
                visited[nxt] = True # 큐에 넣기 전에 방문 처리
                queue.append((nxt, dist + 1))
                
    # 큐를 다 돌았는데도 목적지에 도달하지 못한 경우
    return -1

print(bfs(first, last))