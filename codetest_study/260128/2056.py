# https://www.acmicpc.net/problem/2056
# input 값 받아들여서 graph?로 우선순위 정해 진행하기
# sol1) 우선순위 시간 구하기 -> 각 dfs 구하고 가장 긴 시간 : result?
# sol2) bool list로 작업여부 판단, graph['이후작업'] = [이전 작업들] 구조로 구성
#       이전 작업들이 완료되었다면 time[이후작업] += max(time[이전 작업들])
#       reverse tree로 bfs구현하는 느낌

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N = int(input())

time = []
require = defaultdict(list)
sequence = deque()
for _ in range(N):
    node_info = list(map(int,input().split()))
    time.append(node_info[0])
    if node_info[1] > 0:
        require[node_info[0]] += node_info[2:]
    else: #실행 우선 순위 높음
        sequence.append(node_info[0])

import sys
input = sys.stdin.readline

# N 입력
N = int(input())

# dp[i]: i번 작업이 완료될 때까지 걸리는 최소 시간
# 인덱스 편의를 위해 N+1 크기로 생성
dp = [0] * (N + 1)

for i in range(1, N + 1):
    # 입력: 시간, 선행작업 개수, 선행작업 번호들...
    info = list(map(int, input().split()))
    
    time = info[0]
    pre_count = info[1]
    
    # 선행 작업이 없는 경우
    if pre_count == 0:
        dp[i] = time
    else:
        # 선행 작업들 중 가장 늦게 끝나는 시간(max)을 찾아서 더함
        # info[2:]가 선행 작업들의 번호 리스트임
        max_pre_time = 0
        for pre_task in info[2:]:
            max_pre_time = max(max_pre_time, dp[pre_task])
        
        dp[i] = max_pre_time + time

# 모든 작업이 다 끝나야 하므로, dp 배열 중 가장 큰 값이 정답
# (마지막 N번 작업이 꼭 가장 늦게 끝난다는 보장이 없으므로 max(dp)여야 함)
print(max(dp))

# N = int(input())
# graph = defaultdict(list)
# worklist = deque()

# time = [0] * (N+1)

# for i in range(1, N+1):
#     line = list(map(int, input().split()))
#     time[i] = line[0]
#     if line[1] > 0:
#         for j in range(2, 2 + line[1]):
#             graph[i].append(j)
#     else:
#         worklist.append(i)

# total = 0
# result = 0
# def dfs():
#     global worklist
#     global total, result
#     work_now = worklist.popleft()
#     total += time[work_now]
#     for i in graph[work_now]:
#         worklist.append(i)
#         dfs()
#     if result < total:
#         result = total
#     total = 0

# dfs()
# print(result)





