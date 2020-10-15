import math
 
N, X, T = (int(x) for x in input().split())
 
print(T*math.ceil(N/X))
