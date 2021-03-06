N = int(input())
#N, A = input().split()

#A = [int(x) for x in input().split()]

_list_a = []
_list_b = []
ans = 10**18
result = 10**18
for i in range(N):
    a,b=(int(x) for x in input().split())
    _list_a.append(a)
    _list_b.append(b)

if _list_a.index(min(_list_a)) != _list_b.index(min(_list_b)):
    print(max(min(_list_a),min(_list_b)))
else:
    for i in range(len(_list_a)):
        for n in range(len(_list_b)):
            if _list_a[i]+_list_b[n] <= ans and i != n:
                ans = _list_a[i]+_list_b[n]
                result = max(_list_a[i],_list_b[n])
            elif _list_a[i]+_list_b[n] <= ans and i == n and _list_a[i]+_list_b[n] <= result :
                ans = _list_a[i]+_list_b[n]
                result = ans
    print(result)




