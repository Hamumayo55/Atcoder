N = int(input())

a_list = []
b_list = []

ans = 'No'
for i in range(N-1):
    a, b=(x for x in input().split())
    a_list.append(a)
    b_list.append(b)

import collections

a_cnt = collections.Counter(a_list)
b_cnt = collections.Counter(b_list)

for i in range(1,N+1):
    if int(a_cnt[str(i)]) + int(b_cnt[str(i)]) == N-1:
        ans = 'Yes'
        break

print(ans)
