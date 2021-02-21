N = input()
M = input()

_max = -1
ans = 0
cnt = 0
for i in list(N):
    if int(i) > _max:
        _max = int(i)

def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out

if int(N) < int(M):
    for i in range(_max+1, int(N)+1):
        ans = Base_n_to_10(N,i)
        if ans <= int(M):
            cnt += 1
else:
    while True:
        ans = Base_n_to_10(N,_max+1)
        _max += 1
        if ans <= int(M):
            cnt += 1
        else:
            break
print(cnt)