# https://www.acmicpc.net/problem/8979
# k번째 국가의 순위 확인 -> k와 다른 나라만 비교하면 된다!
# 순위가 같다 -> 차피 k번째 국가의 순위만 확인하면 됨 
#           -> 이겼다고 가정해 계산

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
k_index = 0
medal = [[0 for _ in range(4)]]
for i in range(1, n+1):
    country = list(map(int, input().split()))
    if country[0] == k: k_index = i 
    medal.append(country)

k = k_index
better_than_k = 0
for i in range(1, n+1):
    if i!=k:
        if medal[i][1] != medal[k][1]:
            if medal[i][1] > medal[k][1]:
                better_than_k += 1
        elif medal[i][2] != medal[k][2]:
            if medal[i][2] > medal[k][2]:
                better_than_k += 1
        elif medal[i][3] != medal[k][3]:
            if medal[i][3] > medal[k][3]:
                better_than_k += 1
    else:
        pass

print(better_than_k+1)
# print(medal)
# print(k)