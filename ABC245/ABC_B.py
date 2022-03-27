N = int(input())
#s,w=(int(x) for x in input().split())

A = [int(x) for x in input().split()]
A.sort()


set_a = set(A)

ans = 0

for i in set_a:
    if ans != i and ans < i:
        break
    else:
        ans += 1

print(ans)