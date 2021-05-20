N = int(input())

mnt = {}

for i in range(N):
    S, T = input().split()
    mnt[S] = int(T)

sort_mnt = sorted(mnt.items(), key=lambda x:x[1])

print(sort_mnt[-2][0])