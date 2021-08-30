N = input()
#a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]
X, Y = N.split(".")

if int(Y) >= 0 and int(Y) <= 2:
    print(str(X)+"-")
elif int(Y) >= 3 and int(Y) <= 6:
    print(str(X))
else:
    print(str(X)+"+")
