import sys

n, m, k = map(int, sys.stdin.readline().split())
time = list(map(int, sys.stdin.readline().split()))
time.sort()

start = 0
end = n

while(start <= end):
    mid = (start+end)//2
    total_time = 0
    for i in range(n-1, 0, -mid):
        total_time += time[i]
    
    if total_time > m:
        