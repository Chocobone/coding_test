# import sys

# n, m, k = map(int, sys.stdin.readline().split())
# time = list(map(int, sys.stdin.readline().split()))
# time.sort()

# start = 0
# end = n

# while(start <= end):
#     mid = (start+end)//2
#     total_time = 0
#     for i in range(n-1, 0, -mid):
#         total_time += time[i]
    
#     if total_time > m:
        

import sys
input = sys.stdin.readline 

# N, M, K 입력
try:
    N, M, K = map(int, input().split())
except:
    # 입력이 없거나 형식이 다를 경우를 대비하여 0을 출력하고 종료 (선택적)
    print(0)
    sys.exit()

if N > 0:
    A = list(map(int, input().split()))
    A.sort()
else:
    print(0)
    sys.exit()

# DP 배열 (i번째까지 시청하는 최소 시간)
dp_times = [] 
max_count = 0 # 최대 시청 가능한 애니메이션 개수

for i in range(N):
    # A[0]부터 A[i]까지 i+1개의 애니메이션 고려

    if i < K:
        current_time = A[i]
    else:
        # A[i]를 포함한 K개 묶음의 시간 (A[i]) + 이전 K개 제외한 최소 시간 (dp_times[i-K])
        current_time = dp_times[i - K] + A[i]
    
    # 총 시청 시간이 M을 초과하는지 확인
    if current_time <= M:
        dp_times.append(current_time)
        max_count = i + 1 # i+1개의 애니메이션 시청 가능
    else:
        break

print(max_count)