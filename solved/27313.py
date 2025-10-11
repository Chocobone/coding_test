import sys
# 입력 함수를 sys.stdin.readline으로 설정하여 입력 속도를 높입니다.
input = sys.stdin.readline 

# N, M, K 입력 (N: 애니 개수, M: 최대 시간, K: 동시 시청 최대 개수)
try:
    N, M, K = map(int, input().split())
except:
    # 입력이 없거나 형식이 다를 경우를 대비하여 0을 출력하고 종료 (선택적)
    print(0)
    sys.exit()

# 애니메이션 길이 리스트 입력 및 정렬
if N > 0:
    A = list(map(int, input().split()))
    A.sort()
else:
    # N=0이면 당연히 0 출력
    print(0)
    sys.exit()

# DP 배열 (i번째까지 시청하는 최소 시간)
# 메모리를 절약하기 위해 DP 배열 대신 리스트에 순차적으로 시간을 저장하여 사용
dp_times = [] 
max_count = 0 # 최대 시청 가능한 애니메이션 개수

for i in range(N):
    # i는 0부터 N-1까지의 인덱스, 현재까지 A[0]부터 A[i]까지 i+1개의 애니메이션 고려

    if i < K:
        # Case 1: 애니메이션 개수가 K개 이하 (인덱스 i가 K-1 미만)
        # 모두 한 묶음으로, A[i]가 시청 시간을 결정
        current_time = A[i]
    else:
        # Case 2: 애니메이션 개수가 K개 초과 (인덱스 i가 K-1 이상)
        # A[i]를 포함한 K개 묶음의 시간 (A[i]) + 이전 K개 제외한 최소 시간 (dp_times[i-K])
        # dp_times[i-K]는 A[i-K]까지 시청한 최소 시간입니다.
        current_time = dp_times[i - K] + A[i]
    
    # 총 시청 시간이 M을 초과하는지 확인
    if current_time <= M:
        dp_times.append(current_time)
        max_count = i + 1 # i+1개의 애니메이션 시청 가능
    else:
        # M을 초과하면 이후의 애니메이션은 시청 불가능
        break

# 결과 출력
print(max_count)