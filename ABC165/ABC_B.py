import math
from decimal import Decimal

N = int(input())
#a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

cnt = 0
ans = 100

while True:
    cnt += 1

    ans = ans + ans//100

    if ans >= N:
        break

print(cnt)