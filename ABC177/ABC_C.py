from itertools import accumulate
N=int(input())
A=list(map(int,input().split()))
A_riv=list(accumulate(A[::-1]))[::-1]

ans=0
mod=10**9+7

for i in range(N-1):
    ans+=A[i]*A_riv[i+1]%mod
    print(A[i],A_riv[i+1])
print(ans%mod)
#print(A[::-1])
