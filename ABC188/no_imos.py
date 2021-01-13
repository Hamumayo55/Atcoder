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
    for n in range(start[i],end[i]):
        table[n] += 1

for i in table:
    if max_table < i:
        max_table = i

print(max_table)