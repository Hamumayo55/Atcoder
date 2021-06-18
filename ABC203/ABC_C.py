N,K=(int(x) for x in input().split())
set_A = set()
dict_A = {}

for i in range(N):
    a, b = (int(x) for x in input().split())

    if a not in set_A:
        dict_A[a] = b
        set_A.add(a)
    else:
        dict_A[a] += b

a = sorted(dict_A.items())

for i in a:
    if K >= i[0]:
        K += i[1]
    else:
        break

print(K)

