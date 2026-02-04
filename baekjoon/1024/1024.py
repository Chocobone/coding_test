import sys
input = sys.stdin.readline

result = []
n, l = map(int, input().split())

while(1):
    x = (n-l*(l+1)/2)/l
    
    if x < -1:
        break
    if l > 100:
        break

    if x == int(x):
        for i in range(1, l+1):
            result.append(int(x+i))
        break
    else:
        l += 1

if len(result) > 0 :
    print(*result)
else :
    print(-1)

    
# sol 1:
# result = -1
# for i in range(l, (n//2) + 1):
#     if(i > 100):
#         break
#     elif (n-i*(i+1)//2)//i == (n-i*(i+1)/2)/i :
#         result = (n-i*(i+1)//2)//i
#         l = i
#         break

# if result < -1:
#     print(-1)
# else:        
#     for j in range(1, l+1):
#         print(result+j, end=' ')
