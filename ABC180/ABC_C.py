import math
N = int(input())

ans = []
for i in range(1, int(math.sqrt(N))+1):
    m = 0
    if N%i == 0:
        m = N/i
        ans.append(i)
        if m != i:
            ans.append(int(m))
ans.sort()
for n in range(len(ans)):
    print(ans[n])
