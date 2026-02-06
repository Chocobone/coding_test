#https://www.acmicpc.net/problem/1612

import sys

N = int(sys.stdin.readline())

find_num = False

if N%2 == 0 or N%5 == 0:
    pass
# elif N != 11 and N%11 == 0:
#     pass
else:
    num = 1
    length = 1
    while True:
        if int(num)%N == 0:
            find_num = True
            break
        num = (num * 10 + 1) % N
        length += 1
        # num = '1'
        # if int(num)%N == 0:
            # find_num = True
            # break
        # num += '1'

if find_num:
    print(length)
else:
    print(-1)