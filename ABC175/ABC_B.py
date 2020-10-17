import itertools
S=input()
a=map(int, input().split())
cnt = 0
for i in itertools.combinations(a,3):
    if i[0] != i[1] and i[0] != i[2] and i[1] != i[2]:
        if i[0] + i[1] > i[2] and i[1] + i[2] > i[0] and i[0] + i[2] > i[1] :
            cnt += 1
print(cnt)
