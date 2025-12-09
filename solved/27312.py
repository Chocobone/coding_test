# https://www.acmicpc.net/problem/27312

# list[m][n]에서 완전히 겹치지 않는 list[m+1]을 만들어라
# q번 질문 할 수 있다
# m<=q<=n
# ? k i : list[k][i]를 출력
# ! (list[m+1]) : list[m+1]을 출력, len(list[m+1])== n

# testcase:
# 3 3 3
# 2 2 2
# ans= [[1,1,1],
#       [1,2,1],
#       [1,1,2]]

import sys

m, n, q = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

ans = []
for i in range(m):
    sys.stdout.write('? '+ str((i)%m + 1) + ' ' + str(i+1)+'\n')
    sys.stdout.flush()
    ans.append(int(sys.stdin.readline()))

result = a
for i in range(m):
    if (result[i]==ans[i]):
        result[i] = (result[i])%a[i] + 1

result_str = ''
for i in result:
    result_str += ' '+str(i)

sys.stdout.write('!' + result_str + '\n')
sys.stdout.flush()