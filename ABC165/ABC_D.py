#N = int(input())
A,B,N=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

if B > N:
    print((A*N//B) - A*(N//B))
elif B <= N:
    print((A*(B-1)//B) - A*((B-1)//B))