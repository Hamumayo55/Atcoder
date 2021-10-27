H, W, X, Y = (int(x) for x in input().split())

x = X - 1
y = Y - 1

masu = []

ans = 1

for i in range(H):
    _input = list(input())
    masu.append(_input)

# 上側のマス
for i in range(1,x+1):
    if masu[x-i][y] != '#':
        ans += 1
    else:
        break

# 下側のマス
for i in range(1,H-x):
    if masu[x+i][y] != '#':
        ans += 1
    else:
        break

# 左側のマス
for i in range(1,y+1):
    if masu[x][y-i] != '#':
        ans += 1
    else:
        break

# 右側のマス
for i in range(1,W-y):
    if masu[x][y+i] != '#':
        ans += 1
    else:
        break

print(ans)