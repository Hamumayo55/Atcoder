from decimal import Decimal

A = [int(x) for x in input().split()]

if Decimal(A[0])**Decimal(0.5) + Decimal(A[1])**Decimal(0.5) < Decimal(A[2])**Decimal(0.5):
    print("Yes")
else:
    print("No")

