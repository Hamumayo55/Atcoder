N = int(input())
#a=(int(x) for x in input().split())

gacha = []

# A = [int(x) for x in input().split()]
for i in range(N):
    s = input()
    gacha.append(s)

print(len(set(gacha)))

