#https://www.acmicpc.net/problem/34825

# 두 점의 수선의 발 길이가 같은 직선 구하기

import sys
input = sys.stdin.readline

xa, ya = map(int, input().split())
xb, yb = map(int, input().split())

x_mid = (xa + xb)/2
y_mid = (ya + yb)/2

