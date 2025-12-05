import sys
import math

m, n = map(int, sys.stdin.readline().split())

prime = [True for _ in range(n+1)]
prime[0] = False
prime[1] = False
for i in range(2, int(math.sqrt(n))+1):
    if prime[i]:
        for j in range(2*i, n+1, i):
            prime[j] = False

lst = []
for idx, b in enumerate(prime):
    if b:
        lst.append(idx)
    
for i in range(len(lst)):
    if lst[i] >= m:
        lst = lst[i:]
        break

for i in lst:
    print(i)