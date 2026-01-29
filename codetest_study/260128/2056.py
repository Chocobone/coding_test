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





