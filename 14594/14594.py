import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

room_wall = [1] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, b):
        room_wall[i] = 0

print(room_wall.count(1) - 1)