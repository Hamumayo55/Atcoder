N = int(input())
#a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

cnt = 0
ans = 0
for i in range(1,N+1):
    cnt += i
    if cnt >= N:
        ans = i
        break
print(ans)