# https://www.acmicpc.net/problem/8982
# y축 -> x축의 순서로 이동

import sys
input = sys.stdin.readline

N = int(input())
# (x_len[i], y_len[i]), (x_len[i], y_len[i+1])
x_len = []
y_len = []

x_start, y_start = map(int, input().split()) # 0, 0
for i in range(N-1):
    x, y = map(int, input().split())
    if i%2 == 0:
        y_len.append(y-y_start)
    else:
        x_len.append(x-x_start)

K = int(input())
for _ in range(K):
    hole_start, hole_y, hole_end, _ = map(int, input().split())
    for i in range(x_len.index(hole_start))


print(x_len)
print(y_len)