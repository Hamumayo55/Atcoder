N, K = input().split()
A = (int(x) for x in input().split())

A_1 = sorted(A)
cnt = 0
for i in range(int(K)):
    cnt += A_1[i]
print(cnt)
