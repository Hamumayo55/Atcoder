
#N = int(input())
#s,w=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]

_list = []

for i in range(4):
    N = input()
    _list.append(N)

if len(set(_list)) == 4:
    print("Yes")
else:
    print("No")