import sys
input = sys.stdin.readline

S = input().rstrip()
N = len(S)
ans = sys.maxsize
found = False

# a1의 길이: i, a2의 길이: j
# 숫자는 10^9 미만이어야 하므로 길이는 최대 9~10입니다.
for i in range(1, min(N, 11)):
    for j in range(1, min(N - i, 11)):
        # 1. 초기 두 수 파싱
        s1 = S[:i]
        s2 = S[i:i+j]
        
        # str의 첫 숫자가 0이면 계산 불가
        if (len(s1) > 1 and s1.startswith('0')) or (len(s2) > 1 and s2.startswith('0')):
            continue
        
        a1 = int(s1)
        a2 = int(s2)
        
        # 문제 조건: 1 <= a_i < 10^9
        if a1 >= 10**9 or a2 >= 10**9: continue
        
        # 공차가 양수여야 함
        d = a2 - a1
        if d <= 0: continue
        
        # 현재 상태: a1, a2 까지 찾음. 
        # 이제 남은 문자열이 a3(마지막 항)이 될 수도 있고, 
        # a3가 등차수열의 다음 항이고 그 뒤에 a4가 있을 수도 있음.
        
        curr_val = a2
        idx = i + j
        
        # 등차수열 진행 루프
        while idx < N:
            # ---------------------------------------------------
            # [Case A] 현재까지가 a_{n-1}이고, 남은 문자열 전체가 a_n인 경우 확인
            # ---------------------------------------------------
            rest_str = S[idx:]
            
            # 남은 문자열이 너무 길면 10^9 넘어가므로 검사 불필요 (대략 10자리)
            if 0 < len(rest_str) <= 10:
                # Leading Zero 체크
                if not (len(rest_str) > 1 and rest_str.startswith('0')):
                    a_last = int(rest_str)
                    
                    # 마지막 항 조건: < 10^9, 직전 항의 배수, 2배 이상
                    if a_last < 10**9 and a_last % curr_val == 0:
                        f = a_last // curr_val
                        if f >= 2:
                            ans = min(ans, f)
                            found = True
            
            # ---------------------------------------------------
            # [Case B] 등차수열 계속 진행 (다음 항 찾기)
            # ---------------------------------------------------
            next_val = curr_val + d
            if next_val >= 10**9: # 다음 항이 범위 초과면 더 이상 진행 불가
                break
                
            s_next = str(next_val)
            len_next = len(s_next)
            
            # 남은 문자열의 앞부분이 예상되는 next_val과 일치하는가?
            if idx + len_next <= N and S[idx : idx+len_next] == s_next:
                curr_val = next_val
                idx += len_next
            else:
                # 등차수열이 끊기면 이 조합은 더 볼 필요 없음
                break

if found:
    print(ans)
else:
    print(0)