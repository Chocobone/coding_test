# https://www.acmicpc.net/problem/7579

import sys

n, m = map(int, sys.stdin.readline().split())

weight = list(map(int, sys.stdin.readline().split()))
value = list(map(int, sys.stdin.readline().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

