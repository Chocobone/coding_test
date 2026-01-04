#https://www.acmicpc.net/problem/34199

# sol1 : 최소 비용의 2배를 넘지 않도록 패스를 구매(그리디)
# #  p1 < p2
# 1. t1 > t2인 경우 : 무조건 1번 패스를 사는 것이 이득
# 2. t1 == t2인 경우 : 무조건 1번 패스를 사는 것이 이득
# 3. t1 < t2인 경우:
#   t1/p1 < t2/p2라면 2번 패스
#   t1/p1 >= t2/p2라면 1번 패스

# import sys
# input = sys.stdin.readline
# output = sys.stdout.write

# p1, t1, p2, t2 = map(int, input().split())

# is_finished = False
# while(not is_finished):
#     if t1 < t2 and t1/p1 < t2/p2:
#         output("? 2\n")
#     else:
#         output("? 1\n")
#     sys.stdout.flush()
    
#     gangshin = int(input().rstrip())
#     if gangshin == -1:
#         is_finished = True
    
# output("!")
# sys.stdout.flush()

# 문제 : 입력이 10 10 60 200이고
# (74%) 종료 일자가 20인 경우 p2를 사는 것 자체가 최소 비용(20)의 2배를 넘는다(50)

# sol2 : 총 비용이 p2의 절반을 넘을 때 까지는 p1만 사기 
#     -> 

import sys
input = sys.stdin.readline
output = sys.stdout.write

p1, t1, p2, t2 = map(int, input().split())

cost_total = 0

is_finished = False
while(not is_finished):
    if t1 < t2 and t1/p1 < t2/p2 and cost_total >= p2//2:
        output("? 2\n")
        cost_total += p2
    else:
        output("? 1\n")
        cost_total += p1
    sys.stdout.flush()
    
    gangshin = int(input().rstrip())
    if gangshin == -1:
        is_finished = True
    
output("!")
sys.stdout.flush()
