# https://www.acmicpc.net/problem/1021

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))

result = 0
for i in num: # i는 원하는 숫자
    if i == num:
