N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
 
ans = 0
for i in range(N):
    ans += A[i]*B[i]
if ans == 0:
    print("Yes")
else:
    print("No")
