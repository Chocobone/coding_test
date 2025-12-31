# https://www.acmicpc.net/problem/9017
# sol : list 2개로 팀원수/점수 합산해서 계산하면 될듯 함
# prob : 무효된 팀은 없는 취급되어 점수 계산에 영향을 줌 
# -> 1차적으로 카운트해서 6명 이하인 팀을 점수에 영향 안주도록

import sys
input = sys.stdin.readline

t = int(input())
result = []
for _ in range(t):

    n = int(input())
    race = list(map(int, input().split()))
    team_count = [0] * 201 # 총 200개 팀에 대한 계산
    for runner in race:
        team_count[runner] += 1
    
    point_count = [0] * 201     # 각 팀의 점수
    member_count = [0] * 201    # 상위 4명의 점수만 계산하기 위한 count
    fifth_runner = [0] * 201    # 점수가 같을 때 5번째 주자의 rank
    rank = 1
    for runner in race:
        if team_count[runner] == 6:
            member_count[runner] += 1

            if member_count[runner] <= 4:
                point_count[runner] += rank 
            elif member_count[runner] == 5:
                fifth_runner[runner] = rank
            rank += 1

    win_team = 0
    win_point = 10**9
    for i in range(1, 201):
        if team_count[i] == 6:
            # 1) 점수가 적으면 우승팀 갱신
            if point_count[i] < win_point:
                win_team = i
                win_point = point_count[i]
            # 2) 점수가 같으면 5번째 주자 등수 비교 (작은 쪽이 승리)
            elif point_count[i] == win_point:
                if fifth_runner[i] < fifth_runner[win_team]:
                    win_team = i
    print(win_team)

