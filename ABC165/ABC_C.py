import itertools

#N = int(input())
N,M,Q=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]
max_ans = 0
_input = []
A = list(range(1,M+1))

for i in range(Q):
    a = [int(x) for x in input().split()]
    _input.append(a)

for v in itertools.combinations_with_replacement(A,N):
    tmp = 0
    for i in _input:
        if v[i[1]-1] - v[i[0]-1] == i[2]:
            tmp += i[3]
    max_ans = max(max_ans,tmp)
print(max_ans)
#itertools.combinations()