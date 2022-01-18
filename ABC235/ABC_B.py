N = int(input())
#a,b=(int(x) for x in input().split())

A = [int(x) for x in input().split()]
max_h = -1

for i in range(N):
    h = A[i]
    if max_h < h:
        max_h = h
    else:
        break

print(max_h)
