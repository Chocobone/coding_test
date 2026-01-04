# https://www.acmicpc.net/problem/9663
# dfs 사용한 backtracking 문제
# 퀸이 서로 공격할 수 없다 -> 같은 행, 열, 대각선에 위치하지 않는다
# 하나의 행에 고정해놓고

import sys
n = int(sys.stdin.readline())
board = [[True for _ in range(n)] for _ in range(n)]

result = 0
def dfs(row,