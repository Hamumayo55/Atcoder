#N = int(input())
a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

if b / a <= 6 and b / a >= 1:
    print("Yes")
else:
    print("No")