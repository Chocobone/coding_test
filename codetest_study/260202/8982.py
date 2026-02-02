# https://www.acmicpc.net/problem/8982
# y축 -> x축의 순서로 이동

import sys
input = sys.stdin.readline

N = int(input())
# (x_len[i], y_len[i]), (x_len[i], y_len[i+1])
x_len = [0]
y_len = []

x_start, y_start = map(int, input().split()) # 0, 0
for i in range(N-1):
    x, y = map(int, input().split())
    if i%2 == 0:
        y_len.append(y-y_start)
    else:
        x_len.append(x-x_start)

water_total = 0
for i in range(1, len(x_len)):
    water_total += (x_len[i]-x_len[i-1])* y_len[i-1]

K = int(input())
for _ in range(K):
    hole_start, hole_y, hole_end, _ = map(int, input().split())
    hole_loc = x_len.index(hole_start)
    for i in range(hole_loc):
        if y_len



# print(x_len)
# print(y_len)