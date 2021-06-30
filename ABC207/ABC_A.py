#N = int(input())
a,b,c=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

ans = [a+b,b+c,c+a]
print(max(ans))