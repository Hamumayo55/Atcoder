H,W= map(int, input().split())

block = []
min_value = 101
_sum = 0

for i in range(H):
    a = []
    a = input().split()
    if min_value > int(min(a)):
        min_value = int(min(a))
    block.append(a)

for i in range(H):
    for n in range(W):
        _sum += int(block[i][n]) - min_value

print(_sum)
