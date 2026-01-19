# https://www.acmicpc.net/problem/17086
# 상어 간의 최대 안전 거리를 구하라

# 두 상어의 최소 거리는 max(abs(n1-n2), abs(m1-m2))
# sol1) n * m 단의 list를 graph 구조로 변형해서 넣고 서로 비교하기
# prob) 가장 먼 거리를 비교한다 -> 사이에 다른 상어가 있는 경우를 고려해야 함
# sol2) : 

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = list()
for i in range(n):
    shark_map = (list(map(int, input().split())))
    for j in range(m):
        if shark_map[j] == 1:
            graph.append([i+1, j+1])

min_len = 0
for i in range(len(graph)-1):
    for j in range(i+1, len(graph)):
        
        length = max(abs(graph[i][0]-graph[j][0])-1, abs(graph[i][1]-graph[j][1])-1)
        if min_len < length:
            min_len = length

print(length)