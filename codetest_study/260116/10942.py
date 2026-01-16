# https://www.acmicpc.net/problem/10942
# sol1) list slicing + 대칭 비교(홀/짝 나눠서 구현)
# prob: 시간 초과 걸림 - O(NM) > 1s 
# 효율적인 방법 필요

# sol2) + DP
# 길이별 가능한 회문(펠린드롬)을 DP - bottom-up으로 구하기
# 길이가 홀수/짝수인지에 따라 2개의 DP 만들기 - DP_odd, DP_even
# DP_odd[2] = 

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
