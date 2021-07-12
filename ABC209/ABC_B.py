#N = int(input())
N,X=(int(x) for x in input().split())

A = [int(x) for x in input().split()]
_sum = 0
for i in range(N):
    if (i+1) % 2 == 0:
        A[i] = A[i] - 1
    _sum += A[i]
if _sum <= X:
    print("Yes")
else:
    print("No")

