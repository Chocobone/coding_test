# 숫자가 1칸 떨어진 경우 :
# 따로 인쇄 : 7 + 7 | 같이 인쇄 : 5+2*3 = 11
# 숫자가 2칸 떨어진 경우 :
# 따로 인쇄 : 7 + 7 | 같이 인쇄 : 5+2*4 = 13
# 따라서 숫자가 2칸 떨어져 있을 때 까지는 연속해서 인쇄하면 된다

# 인쇄할 논문이 4개 이상 : (ex:1,4,5,8) -> 14 + 11 vs 13 + 13

import sys

n, m = map(int, sys.stdin.readline().split())
paper_now = set(map(int, sys.stdin.readline().split()))
paper_now = list(paper_now) # 중복 제거 후 정렬

paper_print = [i for i in range(1, n+1)]
for i in paper_now:
    paper_print.remove(i)

print(paper_print)


