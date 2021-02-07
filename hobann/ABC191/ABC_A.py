A = [int(x) for x in input().split()]

if A[3]/A[0] >= A[1] and A[3]/A[0] <= A[2]:
    print("No")
else:
    print("Yes")
