from sys import stdin
import math

n = int(stdin.readline())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split(' '))
    dis = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    if(dis==0 and r1==r2):
        print(-1)
    elif(dis > r1+r2 or r1 > r2+dis or r2 > r1+dis):
        print(0)
    elif(r1+r2 == dis or r1 == r2+dis or r2 == r1+dis):
        print(1)
    else:
        print(2)