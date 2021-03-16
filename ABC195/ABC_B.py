import math

A, B, W = (int(x) for x in input().split())

upper = int(math.floor(1000*W/A))
lower = int(math.ceil(1000*W/B))

if lower <= upper:
    print(lower, upper)
else:
    print("UNSATISFIABLE")