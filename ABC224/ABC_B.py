#N = input()
H, W=(int(x) for x in input().split())

masu = []
ans = 'Yes'

for i in range(H):
    _input = [int(x) for x in input().split()]
    masu.append(_input)

for i_1 in range(H-1):
    for i_2 in range(i_1+1, H):
        for j_1 in range(W-1):
            for j_2 in range(j_1+1, W):
                if masu[i_1][j_1] + masu[i_2][j_2] > masu[i_2][j_1] + masu[i_1][j_2]:
                    ans = 'No'
                    break

print(ans)