N = input()
# N, A = input().split()

# A = [int(x) for x in input().split()]

left = N[0::2]
right = N[1::2]

flag = True

for i in left:
    if i.isupper():
        flag = False
        break
for n in right:
    if n.islower():
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")

#print(left)
#print(right)
