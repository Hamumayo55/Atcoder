#N = int(input())
N,K=(int(x) for x in input().split())
 
A = [int(x) for x in input().split()]
sort_A = sorted(A)
 
amari = K%N
ans = K//N
 
if amari == 0:
    for i in range(N):
        print(ans)
else:
    sa = sort_A[0:amari][-1]
    for i in A:
        if i <= sa:
            print(ans+1)
        else:
            print(ans)