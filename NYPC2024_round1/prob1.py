import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    a, b = min(a, b), max(a,b) # a<=b

    if(3*a < b):
        print(-1)
        continue
    else:
        print(math.ceil((b+a)/4))
