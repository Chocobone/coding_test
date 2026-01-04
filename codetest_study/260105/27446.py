# https://www.acmicpc.net/problem/27446
# (missed_page[index+1] - missed_page[index]) < 4면 연속해서 인쇄하는 것이 효과적
# -> greedy로 다음 page와의 간격을 구해 인쇄를 하면 최소 비용!
#

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
page = set(map(int, input().split()))

missed_page = sorted({index for index in range(1, n+1)} - page)
left_page = len(missed_page)

# i번째 missed_page를 연속해 작성할 것인지 여부 확인(그리디)
if len(page) == n:
    print(0)

else:
    ink = 7
    for i in range(left_page - 1):
        page_gap = missed_page[i+1] - missed_page[i]
        if page_gap <= 3:
            ink += page_gap * 2
        else :
            ink += 7

    print(ink)

# # 다음 missed_page까지 연속으로 인쇄하는 것 vs 따로 인쇄하는 것을 비교
# max_ink = 10e9
# def dfs(ink_used, index):
#     global max_ink
#     if index == left_page - 1:
#         if ink_used < max_ink:
#             max_ink = ink_used
#         return
#     else:
#         # 연속해서 인쇄하는 경우
#         dfs(ink_used + 2*(missed_page[index+1] - missed_page[index]), index + 1)
#         # 따로 인쇄하는 경우
#         dfs(ink_used + 7, index+1)

# dfs(7, 0)
# print(missed_page)
# print(max_ink)