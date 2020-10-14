S = input()
T = input()

ans = 10**5
for i in range(len(S) - len(T) + 1):
    tmp = 0
    for n in range(len(T)):
        if S[i+n] == T[n]:
            tmp += 1
    ans = min(ans, len(T)-tmp)
print(ans)
