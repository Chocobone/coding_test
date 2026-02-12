# https://www.acmicpc.net/problem/27448

import sys
input = sys.stdin.readline

N, M, F = map(int, input().split())
wood = [list(input().rstrip()) for _ in range(N)]