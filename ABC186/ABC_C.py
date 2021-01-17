N = int(input())
_sum = 0
for i in range(1, N+1):
  if ('7' not in str(i)) and ('7' not in oct(i)):
    _sum += 1
print(_sum)

