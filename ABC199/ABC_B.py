N = int(input())
#a,b,c=(int(x) for x in input().split())

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

a = 0
b = 1001

for i in range(N):
    if A[i] > a:
        a = A[i]
    if B[i] < b:
        b = B[i]

if a <= b:
    print(b-a+1)
else:
    print(0)