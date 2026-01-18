# https://www.acmicpc.net/problem/10942
# sol1) list slicing + 대칭 비교(홀/짝 나눠서 구현)
# prob: 시간 초과 걸림 - O(NM) > 1s 
# 효율적인 방법 필요

# sol2) + DP
# 길이별 가능한 회문(펠린드롬)을 DP - bottom-up으로 구하기
# dp[i] = 길이가 i인 펠린드롬의 시작지점
# -> 2차원으로 관리, 길이 별로 case를 나눠 관리하기

import sys
input = sys.stdin.readline

N = int(input())
num = [0] + list(map(int, input().split()))

dp = [[0] * (N) for _ in range(N)]
#dp[start][length]

for i in range(1, N):
    dp[i][i] = 1
    dp[i][i+1] = 1 if num[i] == num[i+1] else 0

for i in range(N-1, 0, -1):
    for j in range(i+2, N+1):
        if dp[i+1][j-1] == 1 and num[i] == num[j] :
            dp[i][j] == 1

print(dp)
for _ in range(int(input())):
    S, E = map(int, input().split())
    print(dp[S][E])


# dp[0].append(0)
# for length in range(1, N): 
#     for start in range(1, N-length+1):
#         subnum = num[start:start+length+1]
#         center = (len(subnum)//2)
#         is_felindrom = True
#         # print(subnum, subnum[center])
#         for i in range(center):
#             if subnum[i] != subnum[-1-i]:
#                 is_felindrom = False
#                 break
#         if is_felindrom:
#             dp[length+1].append(start)

# print(dp)

# M = int(input())
# for _ in range(M):
#     S, E = map(int, input().split())

#     leng = E - S + 1
        
#     if leng == 1 or S in dp[leng]:
#         print(1)
#     else:
#         print(0)


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
    #         print(0)
