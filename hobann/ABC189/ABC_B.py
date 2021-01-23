N,X = input().split()
ans = False
result = 0
cnt = 0

for i in range(int(N)):
    B = [int(x) for x in input().split()]
    result += B[0]*B[1]

    if result > int(X)*100:
        ans = True
        cnt = i+1
        break

if ans:
    print(cnt)
else:
    print(-1)