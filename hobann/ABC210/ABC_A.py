#N = int(input())
n,a,x,y=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]
ans = 0
for i in range(n):
    if (i+1) > a:
        ans += y
    else:
        ans += x

print(ans)