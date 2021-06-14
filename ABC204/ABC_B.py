N = int(input())
#x,y=(int(x) for x in input().split())
A = [int(x) for x in input().split()]

cnt = 0

for i in A:
    if i > 10:
        cnt += abs(10 - i)

print(cnt)