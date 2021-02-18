from decimal import Decimal
import math

A, B = input().split()

a = int(A)
b = Decimal(B)

print(math.floor(a*b))