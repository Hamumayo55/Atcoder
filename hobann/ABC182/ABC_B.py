N = input()
A = input().split()
cnt = 0
max_k = max(A)
ans = 0
m = 0
for i in range(2, int(max_k)+1):
    flag = 0
    for n in range(int(N)):
        if int(A[n]) % i == 0:
            flag += 1
    if flag >= 1and cnt <= flag :
        m = i
        cnt = flag
        ans = i
print(ans)
