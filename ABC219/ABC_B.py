S1 = input()
S2 = input()
S3 = input()

S = [S1,S2,S3]

T = input()
#a,b=(int(x) for x in input().split())

#a = [int(x) for x in input().split()]

ans = []
for i in T:
    ans.append(S[int(i)-1])

print(''.join(ans)) 
