import itertools
N = input()
array = sum(list(map(int, N)))
ans = 0
if int(N) % 3==0:
    print(0)
else:
    for i in range(1,len(N)):
        for n in itertools.combinations(N,i):
            hoge = sum(list(map(int, list(n))))
            if (array-hoge) % 3 == 0 and ans == 0:
                ans += i
    if ans == 0:
        print(-1)
    else:
        print(ans)
