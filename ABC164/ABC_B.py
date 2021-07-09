#N = int(input())
a,b,c,d=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

turn = 1
attack = 0

while a > 0 and c > 0:
    if turn % 2 == 0:
        a -= d
        attack = 0
    else:
        c -= b
        attack = 1
    turn += 1

if attack == 1:
    print("Yes")
else:
    print("No")