K = int(input())
a,b=(str(x) for x in input().split())

# A = [int(x) for x in input().split()]
def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out

ans1 = Base_n_to_10(a,K)
ans2 = Base_n_to_10(b,K)
print(ans1*ans2)