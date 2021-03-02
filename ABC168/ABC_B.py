K = int(input())
N = input()

if len(N) <= K:
    print(N)
else:
    print(N[0:K]+str("..."))
