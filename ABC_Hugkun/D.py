import math

N = int(input())
#a,b=(int(x) for x in input().split())
 
a = [int(x) for x in input().split()]

sum_bugs = 0
not_bugs = 0

for i in range(N):
    if a[i] == 0:
        not_bugs += 1
    else:
        sum_bugs += a[i]

print(math.ceil(sum_bugs/(N-not_bugs)))

