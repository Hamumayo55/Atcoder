#N = int(input())
#N, A = input().split()

A = [int(x) for x in input().split()]

diff = 0

if A[0] >= A[3]:
    print(A[3])
elif A[0] + A[1] >= A[3]:
    print(A[3]-A[1])
else:
    diff = A[3] - (A[0]+A[1])
    print(A[0] - diff)