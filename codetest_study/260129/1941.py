# https://www.acmicpc.net/problem/1941
# S, Y로 채워져 있는 array에서 
# 가로/세로로 인접하게 7개 뽑고
# 그 중 S가 더 많아야 함
# sol1) visited 행렬 사용해 dfs 구현 -> 모서리부터 좁혀가면서 

import sys
input = sys.stdin.readline

seat = [list(input().rstrip()) for _ in range(5)]
