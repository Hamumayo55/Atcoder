import math

A = [int(x) for x in input().split()]

if A[0] == 1 or A[1] == 1:
    print(1)
else:
    print(math.ceil((A[0]*A[1])/2))