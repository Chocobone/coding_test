# https://www.acmicpc.net/problem/14889

# 1. n/2명씩 팀을 짜는 알고리즘(nCn/2)

# 2. 각 팀의 점수를 구하기
# for문을 인원에 맞게 조정해야 함
import sys
input = sys.stdin.readline

n = int(input())

score = []
diff = 2000
for _ in range(n):
    score.append(list(map(int, input().split())))

def team_divide(n, i):
    team_red = tuple()
    
