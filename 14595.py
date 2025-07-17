import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

#1st : 14594 method(failed)
#room_wall = [1] * (n+1)

# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     for i in range(a, b):
#         room_wall[i] = 0

#2nd : using set(failed)
broken_wall = set()
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, b):
        broken_wall.add(i)


print(n - len(broken_wall))