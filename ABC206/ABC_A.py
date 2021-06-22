import math

N = int(input())
#a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

if math.floor(N*1.08) > 206:
    print(":(")
elif math.floor(N*1.08) == 206:
    print("so-so")
else:
    print("Yay!")