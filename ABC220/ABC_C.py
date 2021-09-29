N = int(input())
#a,b=(int(x) for x in input().split())

A = [int(x) for x in input().split()]
X = int(input())

sum_A = sum(A)

cnt = (X // sum_A)*N
amari = X % sum_A

_sum = 0
for i in A:
    _sum += i
    cnt += 1
    if _sum > amari :
        break

print(cnt)