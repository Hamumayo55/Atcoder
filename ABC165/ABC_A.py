K = int(input())
a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

ans = "NG"

for i in range(a,b+1):
    if i % K == 0:
        ans = "OK"
        break
print(ans)