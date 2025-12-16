import sys
input = sys.stdin.readline

a, x = map(int, input().split())

result = list(map(int, input().split()))
for i in result:
    if i < x:
        print(i, end=' ')