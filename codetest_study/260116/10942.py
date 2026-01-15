# https://www.acmicpc.net/problem/10942
# list slicing + 대칭 비교(홀/짝 나눠서 구현)

import sys
input = sys.stdin.readline

N = int(input())
num = [0] + list(map(int, input().split()))
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    subnum = num[S:E+1]

    # if len(subnum)%2 == 1:
    center = (len(subnum)//2)
    is_felindrom = True
    # print(subnum, subnum[center])
    for i in range(center):
        if subnum[i] != subnum[-1-i]:
            is_felindrom = False
            break
    
    if is_felindrom:
        print(1)
    else:
        print(0)
    # else:
    #     center = (len(subnum)//2)
    #     is_felindrom = True
    #     # print(subnum, subnum[center])
    #     for i in range(center):
    #         if subnum[i] != subnum[-1-i]:
    #             is_felindrom = False
    #             break
        
    #     if is_felindrom:
    #         print(1)
    #     else:
            # print(0)
