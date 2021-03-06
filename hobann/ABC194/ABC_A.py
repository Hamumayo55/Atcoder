#N = int(input())
a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

if a+b >= 15 and int(b) >= 8:
    print(1)
elif a+b >= 10 and int(b) >= 3:
    print(2)
elif (a)+b >= 3:
    print(3)
else:
    print(4)

