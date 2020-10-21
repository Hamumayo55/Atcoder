x = input().split()
cnt = 0
su = 0
for i in range(len(x)):
    cnt += int(x[i])
    su += i +1
print(su - cnt)
