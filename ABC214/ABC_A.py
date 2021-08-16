N = int(input())
#s,w=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

if N <= 125 and N >= 1:
    print(4)
elif N <= 211 and N >= 126:
    print(6)
else:
    print(8)