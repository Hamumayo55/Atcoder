#N = int(input())
N,K,A=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

ans = (A-1+K)%N
if ans == 0:
    print(N)
else:
    print(ans)