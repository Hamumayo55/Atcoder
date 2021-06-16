N,K=(int(x) for x in input().split())

ans = 0

for i in range(1,N+1):
    for j in range(1,K+1):
        ans += int(str(i)+str(0)+str(j))
print(ans)