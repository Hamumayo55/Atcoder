N = int(input())
S = input()

# A = [int(x) for x in input().split()]

ans = 0

for i in range(N):

    if S[i] == '1':
        ans = i
        break

if ans % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")