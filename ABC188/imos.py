N = int(input())

start = []
end = []
table = [0,0,0,0,0,0,0]
max_table = 0 
for i in range(N):
    _s, _e = map(int, input().split())
    start.append(_s)
    end.append(_e)

for i in range(N):
    table[start[i]] += 1
    table[end[i]] -= 1

for i in range(len(table)):
    if i > 0:
        table[i] += table[i-1]

for i in table:
    if max_table < i:
        max_table = i

print(max_table)