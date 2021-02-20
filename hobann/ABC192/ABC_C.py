N,K = input().split()

ans = N

def f(_input,k):
    A = ''.join(sorted(list(_input)))
    B = ''.join(sorted(list(_input),reverse=True))
    result = int(B) - int(A)
    return result

for i in range(int(K)):
    ans = f(str(ans),K)

print(ans)