import itertools
import collections

N = int(input())
A = [int(x) for x in input().split()]

count_A = collections.Counter(A)
set_A = set(A)
ans = 0

for (i,j) in itertools.combinations(set_A, 2):
    ans += count_A[i]*count_A[j]*(i-j)**2

print(ans)