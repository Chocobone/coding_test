# https://www.acmicpc.net/problem/13018

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if N == K : print("Impossible")

else:
    result = [0] * N
    for i in range(N-K, N):
        result[i] = i+1
    
    for i in range(N-K-1):
        result[i] = i+2
    
    result[N-K-1] = 1

    print(' '.join(str(x) for x in result))