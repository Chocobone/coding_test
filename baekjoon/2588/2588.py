import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

b3 = b%10
b2 = (b%100 - b3)//10
b1 = b//100

print(a*b3)
print(a*b2)
print(a*b1)
print(a*b)