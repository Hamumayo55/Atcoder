#N = int(input())
import math
a,b,c,d=(int(x) for x in input().split())

ans = -1
cnt = 0

if b/c >= d:
    print(ans)
else:
    ans = (-a)/(b-d*c)
    print(math.ceil(ans))
