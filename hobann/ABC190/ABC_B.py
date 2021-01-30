#N = int(input())
A = [int(x) for x in input().split()]

ok = False

for i in range(A[0]):
    B = [int(x) for x in input().split()]
    if B[0] < A[1]:
        if B[1] > A[2]:
            ok = True
            break

if ok:
    print("Yes")
else:
    print("No")