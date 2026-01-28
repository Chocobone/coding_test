# https://www.acmicpc.net/problem/32294
# 수열 밖 : x < 1 or x > n
# left : (수열을 벗어나기 위해) 좌측으로 남은 칸, right : 우측으로 남은 칸
# 좌측으로 갈 때의 최소 시간(dp_l) vs 우측으로 갈 때의 최소시간 비교(dp_R)
# dp? bfs? -> BFS!

import sys
import heapq
input = sys.stdin.readline

N = int(input())
# A: 점프 거리, B: 점프 비용
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# reverse_adj[도착지] = [출발지1, 출발지2, ...]
reverse_adj = [[] for _ in range(N)]
INF = sys.maxsize
dist = [INF] * N

pq = []

for i in range(N):
    can_exit = False
    
    # 왼쪽으로 점프
    left_dest = i - A[i]
    if left_dest < 0: # 범위 밖 -> 탈출 가능
        can_exit = True
    else:
        # 범위 안 -> 역방향 간선 추가 (left_dest에서 i로 오는 것으로 기록)
        reverse_adj[left_dest].append(i)
        
    # 오른쪽으로 점프
    right_dest = i + A[i]
    if right_dest >= N: # 범위 밖 -> 탈출 가능
        can_exit = True
    else:
        # 범위 안 -> 역방향 간선 추가
        reverse_adj[right_dest].append(i)
        
    if can_exit:
        # 이미 큐에 들어가 있거나 더 짧은 경로가 있다면 무시되겠지만,
        # 초기화 단계에서는 가장 먼저 탈출하는 비용이 B[i]임이 확실함.
        dist[i] = B[i]
        heapq.heappush(pq, (B[i], i))

while pq:
    current_time, curr = heapq.heappop(pq)

    # 이미 처리된 경로보다 더 긴 시간이면 스킵
    if dist[curr] < current_time:
        continue

    # curr로 점프해 들어올 수 있는 이전 노드들(prev) 확인
    for prev in reverse_adj[curr]:
        # prev에서 탈출하는 시간 = (prev에서 한번 점프하는 시간 B[prev]) + (curr에서 탈출하는 시간)
        new_time = current_time + B[prev]
        
        if new_time < dist[prev]:
            dist[prev] = new_time
            heapq.heappush(pq, (new_time, prev))

print(*(dist))
