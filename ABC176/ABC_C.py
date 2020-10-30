N = int(input())
A = input().split()

cnt = 0
for i in range(N-1):
    s = 0
    s = int(A[i+1]) - int(A[i])
    if s < 0:
        A[i+1] = int(A[i+1]) - s
        cnt += abs(s)
print(cnt)
