import itertools

N = int(input())

zahyou = []
cnt = 0
for i in range(N):
    _zahyou = []
    x,y = map(int,input().split())
    _zahyou.append(x)
    _zahyou.append(y)

    zahyou.append(_zahyou)

for i in list(itertools.combinations(zahyou,2)):
    judge = (i[1][1] - i[0][1])/(i[1][0] - i[0][0])

    if judge >= -1 and judge <= 1:
        cnt += 1

print(cnt)


