A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0

if 500 <= X:
    A_loop = X//500
    if A_loop > A:
        A_loop = A

    for i in range(1,A_loop+1):
        amari = X - 500*i
        
        if amari <= 0:
            break

        B_loop = amari//100
        if B_loop > B:
            B_loop = B

        for m in range(1,B_loop):
            amari = X - (500*i + )
