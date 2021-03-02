import math
from decimal import Decimal

A = [int(x) for x in input().split()]

kakudo = abs(30*A[2] + 0.5*A[3] - 6*A[3])

if kakudo > 180:
    kakudo = 360 - kakudo

degree = Decimal(math.cos(math.radians(kakudo)))

ans = A[0]**2 + A[1]**2 - 2*A[0]*A[1]*degree
print(ans**Decimal(0.5))