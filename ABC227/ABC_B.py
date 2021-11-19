N = int(input())
#s,w=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]
S = [int(x) for x in input().split()]

ans = 0

for idx in range(len(S)):
    flag = True
    for b in range(1, S[idx]):
        if (S[idx]-3*b)%(4*b+3) == 0 and flag and (S[idx]-3*b) != 0:
            ans += 1
            flag = False
            
print(len(S)-ans)
