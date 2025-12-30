# https://www.acmicpc.net/problem/1446

# dp[d] = d까지 갔을 때의 최소값으로 정의해 푸는게 나을듯?
import sys
input = sys.stdin.readline

# sol 1 : 각 지름길이 줄여주는 거리의 합이 가장 크도록 하면 된다
# 필터링으로 "사용 가능한 " 지름길 중에서만 고르기
# prob : greedy 형식으로 풀지 못하는 반례 존재
# 2 10000
# 0 10000 9999
# 1 9999 1

# n, d = map(int, input().split())
# road = [[0,0,0]]
# for _ in range(n):
#     shortcut = list(map(int, input().split()))
#     # 지름길이 원래 길이보다 길거나 도착지를 넘는 경우 추가하지 않음
#     if (shortcut[1] - shortcut[0] > shortcut[2]) and shortcut[1] <= d:
#         shortcut[2] = ((shortcut[1] - shortcut[0]) - shortcut[2])
#         #shortcut을 사용해 줄일 수 있는 거리를 list에 추가
#         road.append(shortcut)
# road.sort()

# # 시작 위치, 도착 위치가 같은 지름길이 있으면 줄여주는 거리가 
# # 큰 놈만 남기기
# pop_shortcut = []
# for i in range(len(road)-1):
#     for j in range(i+1, len(road)):
#         if road[i][0] == road[j][0] and road[i][1] == road[j][1]:
#             if road[i][2] >= road[j][2]:
#                 pop_shortcut.append(j)
#             else:
#                 pop_shortcut.append(i)

# pop_shortcut.sort(reverse=True)
# for i in pop_shortcut:
#     road.pop(i)

# # dp[i][0] : i번째까지 체크했을 때의 최대로 줄인 거리
# # dp[i][1] : i번째까지 체크했을 때의 위치
# dp = [[0 , 0] for _ in range(len(road))] 
# dp[1][0] = road[1][2]
# dp[1][1] = road[1][1]
# for i in range(2, len(road)):
#     if dp[i-1][1] <= road[i][0]:
#         dp[i][0] = dp[i-1][0] + road[i-1][2]
#         dp[i][1] = road[i][1]
    
#     else:
#         if road[i][2] > dp[i-1][0]:
#             dp[i][0] = road[i][2]
#             dp[i][1] = road[i][1]
#         else: 
#             dp[i][0] = dp[i-1][0]
#             dp[i][1] = dp[i-1][1]
    
# sol : dp[i] = i까지 걸리는 최소 운전 거리
# dp[i] = dp[i-1] + 1
# dp[i] = min(dp[i-1] + 1 , )

n, d = map(int, input().split())
road = [[0,0,0]]
for _ in range(n):
    shortcut = list(map(int, input().split()))
    # 지름길이 원래 길이보다 길거나 도착지를 넘는 경우 추가하지 않음
    if (shortcut[1] - shortcut[0] > shortcut[2]) and shortcut[1] <= d:
        road.append(shortcut)
road.sort()

# 시작 위치, 도착 위치가 같은 지름길이 있으면 줄여주는 거리가 
# 큰 놈만 남기기
# 안쓰니까 맞았다... 왤까....
# pop_shortcut = []
# for i in range(len(road)-1):
#     for j in range(i+1, len(road)):
#         if road[i][0] == road[j][0] and road[i][1] == road[j][1]:
#             if road[i][2] >= road[j][2]:
#                 pop_shortcut.append(j)
#             else:
#                 pop_shortcut.append(i)

# pop_shortcut.sort(reverse=True)
# for i in pop_shortcut:
#     road.pop(i)

dp = [i for i in range(d+1)]

for i in range(1, d+1):
    dp[i] = min(dp[i], dp[i-1]+1)

    for j in range(len(road)):
        if i == road[j][1]: # i가 도착 지점과 위치가 같을 때
            if dp[i] > dp[road[j][0]] + road[j][2]:
                dp[i] = dp[road[j][0]] + road[j][2]

print(dp[d])
