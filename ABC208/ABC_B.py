import math

P = int(input())
#a,b,c=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

coins = 0

for i in range(10,0,-1):
    tmp = P / math.factorial(i)
    if tmp >= 1:
        P = P - math.floor(tmp)*math.factorial(i)
        coins += math.floor(tmp)

print(coins)
