# https://www.acmicpc.net/problem/11657

# 벨만 - 포드 알고리즘
# 1. 최단경로 탐색
# 2. 가중치가 (-)가 되는 루프 존재 여부 확인
import sys
input = sys.stdin.readline

INF = sys.maxsize

N, M = map(int, input().split())

edge = []
dist = [INF] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    edge.append((a, b, c))

cycle = False
dist[1] = 0
for i in range(N):
    for start, end, cost in edge:
        if dist[start] != INF:
            distance = dist[start] + cost
            if distance < dist[end]:
                if i == N-1:
                    cycle = True
                dist[end] = distance

if cycle:
    print(-1)
else:
    for w in dist[2:]:
        print(w if w != INF else -1)
