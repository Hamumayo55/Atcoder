N = int(input())

A = [int(x) for x in input().split()]

ans = 1

if 0 in A:
    ans = 0
else:
    for i in range(N):
        ans *= A[i]
        if ans > 10**18:
            ans = -1
            break

print(ans)