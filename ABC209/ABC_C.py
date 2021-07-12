N = int(input())
# s,w=(int(x) for x in input().split())

C = [int(x) for x in input().split()]

sort_C = sorted(C)

ans = 1

for i in range(1,N+1):
    if sort_C[i-1] - (i-1) > 0:
        ans = (ans*(sort_C[i-1] - (i-1)))%(10**9+7)
    else:
        ans = 0
        break
print(ans)
