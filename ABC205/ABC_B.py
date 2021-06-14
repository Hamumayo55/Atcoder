N = int(input())
#a,b=(int(x) for x in input().split())
A = [int(x) for x in input().split()]

ans = True

for i in range(1,N+1):
    if i  not in A:
        ans = False
        break

if ans:
    print("Yes")
else:
    print("No")