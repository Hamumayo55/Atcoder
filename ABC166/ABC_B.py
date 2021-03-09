N,K=(int(x) for x in input().split())

sweet_num = []
human = []

for i in range(K):
    d = int(input())
    A = [int(x) for x in input().split()]
    for n in A:
        human.append(n)

set_human = set(human)

print(N-len(set_human))