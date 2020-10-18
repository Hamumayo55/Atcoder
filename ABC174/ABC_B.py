import math
N, D=input().split()
cnt = 0

for i in range(int(N)):
    x, y = input().split()
    dis = math.sqrt((int(x) - 0) ** 2 + (int(y) - 0) ** 2)
    if dis <= int(D):
        cnt += 1
print(cnt)
