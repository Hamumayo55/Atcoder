#N = int(input())
a,b,c=(int(x) for x in input().split())
#A = [int(x) for x in input().split()]

if a == b:
    print(c)
elif a == c:
    print(b)
elif b == c:
    print(a)
elif a == b and b == c:
    print(a)
else:
    print(0)