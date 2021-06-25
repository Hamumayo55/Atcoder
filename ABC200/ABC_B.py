#N   = int(input())
n,k=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

for i in range(k):
    if int(n) % 200 == 0:
        n = int(n/200)
    else:
        n = int(str(n)+str(200))
print(n)