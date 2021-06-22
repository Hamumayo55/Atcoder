import collections

N = int(input())
#a,b=(int(x) for x in input().split())
A = [int(x) for x in input().split()]

a_cnt = collections.Counter(A)
comb = N*(N-1)/2

ans = comb
set_A = set(A)
if len(set_A) != N:
    for i in set_A:
        if a_cnt[i] > 1:
            ans -= a_cnt[i]*(a_cnt[i]-1)/2
print(int(ans))

