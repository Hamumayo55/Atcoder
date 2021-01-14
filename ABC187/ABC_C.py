N = int(input())

S = set(input() for i in range(N))

result = 'satisfiable'

for i in S:
    if "!" + i in S:
        result = i
        break
print(result)