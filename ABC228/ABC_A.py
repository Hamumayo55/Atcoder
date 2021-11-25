#T = input()
S, T, X = input().split()

# A = [int(x) for x in input().split()]

if int(S) < int(T):
    if int(S) <= int(X) and int(X) < int(T):
        print('Yes')
    else:
        print('No')
else:
    if int(S) <= int(X) or int(X) < int(T):
        print('Yes')
    else:
        print('No')
