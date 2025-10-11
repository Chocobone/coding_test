import sys

x, y = map(int, sys.stdin.readline().split())

l = int(sys.stdin.readline())
a = [0] * l
b = [0] * l
c = [0] * l
d = [0] * l
for i in range(l):
    a[i], b[i], c[i], d[i] = map(int, sys.stdin.readline().split())

n = int(sys.stdin.readline())
e = [0] * n
f = [0] * n
for i in range(n):
    e[i], f[i] = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
g = [0] * m
h = [0] * m
for i in range(m):
    g[i], h[i] = map(int, sys.stdin.readline().split())

