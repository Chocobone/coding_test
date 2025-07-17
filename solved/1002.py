import sys
import math

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split(' '))
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if(r1+r2 < distance or r1 > r2+distance or r2 > r1+distance):
        print(0)
    elif(r1+r2 == distance or r1 == r2+distance or r2 == r1+distance):
        print(1)
    else:
        print(2)