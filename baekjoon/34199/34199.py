import sys

p1, t1, p2, t2 = map(int, sys.stdin.readline().split())
#p1 <= p2

m1_cost = t1 / p1
m2_cost = t2 / p2
min_cost = min(m1_cost, m2_cost)

for i in range(1, 1001):
    for j in range(1, 1001):

# d = int(sys.stdin.readline())

# while(d != -1):
#     if(t1>=t2 or t1+1 == d): # p1 <= p2 and t1 >= t2
#         print("? 1")
#         sys.stdout.flush()
#         d -= p1
#     elif(d <= t1 and d <= t2):
#         print("? 1")
#         sys.stdout.flush()
#         d -= p1
#     else: #t1 < t2 and p1 < p2
#         print("? 2")
#         sys.stdout.flush()
#         d -= p2
#     if(d <= 0):
#         d = int(sys.stdin.readline())  

# print("!")
# sys.stdout.flush()