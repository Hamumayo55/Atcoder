A = [int(x) for x in input().split()]
sort_A = sorted(A)

if sort_A[2] - sort_A[1] == sort_A[1] - sort_A[0]:
    print("Yes")
else:
    print("No")