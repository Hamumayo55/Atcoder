import math
N = int(input())
#a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

if N % 100 == 0:
    print(int(N/100))
else:
    print(math.floor(N/100)+1)