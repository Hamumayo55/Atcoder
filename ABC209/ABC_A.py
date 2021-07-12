#N = int(input())
a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]
if b-a >= 0:
    print(b-a+1)
else:
    print(0)