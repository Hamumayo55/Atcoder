#N = int(input())
x,y=(int(x) for x in input().split())
#A = [int(x) for x in input().split()]
zyanken = [0,1,2]
if x == y:
    print(x)
else:
    for i in zyanken:
        if i != x and i != y:
            print(i)


