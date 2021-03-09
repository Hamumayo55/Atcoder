N,M=(int(x) for x in input().split())

H = [int(x) for x in input().split()]

no_good = []
set_nogood = set(no_good)
for i in range(M):
    A,B=(int(x) for x in input().split())
    if H[A-1] > H[B-1]:
        set_nogood.add(B)
    elif H[A-1] < H[B-1]:
        set_nogood.add(A)
    elif H[A-1] == H[B-1]:
        set_nogood.add(A)
        set_nogood.add(B)
print(N - len(set_nogood))