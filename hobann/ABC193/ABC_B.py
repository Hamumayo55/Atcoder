N = int(input())
# N, A = input().split()

# A = [int(x) for x in input().split()]
ans = 10**20
for i in range(N):
    A = [int(x) for x in input().split()]
    A[2] -= A[0]
    if A[2] > 0 and ans > A[1]:
        ans = A[1]

if ans == 10**20:
    print(-1)
else:
    print(ans)




