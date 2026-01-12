#https://www.acmicpc.net/problem/2348
# 배열의 자릿수가 몇자리수인가 -> i를 늘려가며 배열을 만든다
# prob: 자릿수가 중간에 변화하는 경우 i를 늘려가며 진행
# 배열이 추진력 배열인가 
# ex) 989169249498, d = 80, f = 2

import sys
input = sys.stdin.readline

num = input().rstrip() #num은 str형태
n = len(num)

result = sys.maxsize

for len1 in range(1, n):
    for len2 in range(1, n - len1 + 1):
        a1_str = num[:len1]
        a2_str = num[len1:len1+len2]

        a1 = int(a1_str)
        a2 = int(a2_str)
        d = a2 - a1

        index = len1+len2
        num_now = a2
        num_list = [a1, a2]

        win = (d // 10) + 1
        while index < n:
            num_now = num_now + d
            if num_now // 10 != (num_now-d) // 10:
                win += ((num_now) // 10) - ((num_now-d) // 10)
            if index+win >= n or num[index] == '0':
                break
            str_now = num[index:index+win]
            if num_now != int(str_now) and num_now%num_list[-1] != 0:
                break
            elif num_now%num_list[-1] == 0:
                if result > num_now//num_list[-1]:
                    result = num_now//num_list[-1]
                break
            else: # num_now == int() and num_now%num_list[-1] != 0
                index += win
                num_list.append(num_now)
           

print(0 if result == sys.maxsize else result)


# # i는 배열의 길이
# for i in range(1, n): 
#     # 배열 여부 계산을 편하게 하기 위해 list화
#     # if (n%i != 0):
#     #     continue
#     if i > 9 : continue

#     num_list = []
#     error = False
#     d = 0, win = i
#     for win in range(0, n, i):
#         if num[win] == '0':
#             error = True # 앞자리 0
#             break
#         num_now = num[win:win+i]

#         # 등차수열의 자릿수 변화 적용
#         if len(str((int(num_now) + d))) > len(num_now) :
#             win += len(str((int(num_now) + d))) - len(num_now)
#             print(win)
        
#         num_list.append(int(num_now))
#         if len(num_list) == 2:
#             d = num_list[1] - num_list[0]
#             print(d)
        
#     if(len(num_list) < 3) or error: continue

#     d_len = True
#     for j in range(1, len(num_list)-2):
#         if d != num_list[j+1] - num_list[j]:
#             d_len = False
#             break

#     if d_len and num_list[-1]%num_list[-2] == 0:
#         if result > num_list[-1]//num_list[-2]:
#             result = num_list[-1]//num_list[-2]
#     # print(win)


# print(0 if result == sys.maxsize else result)