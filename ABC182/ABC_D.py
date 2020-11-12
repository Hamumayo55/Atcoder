import itertools
N= int(input())
A = list(map(int, input().split()))
cumsum = list(itertools.accumulate(A))
p = 0
maxP = 0
ans = 0
_sum = 0
for n in range(N):
    maxP = max(cumsum[n], maxP)
    ans = max(ans, _sum+maxP)
    _sum += cumsum[n]
print(ans)
