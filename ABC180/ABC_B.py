import numpy
import math

N = int(input())
x = input().split()
a = 0
b = 0
c = 0
for i in range(N):
    a += abs(int(x[i]))
    c = max(c,abs(int(x[i])))
    b += (int(x[i]))**2

print(a)
print(math.sqrt(b))
print(c)
