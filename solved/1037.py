import sys

m = int(sys.stdin.readline())

if(m==1):
    print(int(sys.stdin.readline())**2)

else:
    num = list(map(int, sys.stdin.readline().split()))
    print(min(num)*max(num))