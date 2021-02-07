N, X = input().split()
A = [int(x) for x in input().split()]
ans = []
for i in range(int(N)):
    if A[i] != int(X):
        ans.append(A[i])
print(' '.join(map(str, ans)))