A,B = input().split()

cnt1 = 0
cnt2 = 0
for i in range(3):
    cnt1 += int(A[i])
    cnt2 += int(B[i])

if cnt1 >= cnt2:
    print(cnt1)
else:
    print(cnt2)