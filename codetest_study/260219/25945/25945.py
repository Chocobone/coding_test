# https://www.acmicpc.net/problem/25945

import sys
input = sys.stdin.readline

n = int(input())
port = list(map(int, input().split()))

port.sort()

m = sum(port)
average = m // n
r = m % n   # average+1을 가져야 하는 사람 수

move = 0

for i in range(n):
    if i < n - r:
        move += abs(port[i] - average)
    else:
        move += abs(port[i] - (average + 1))

print(move // 2)
