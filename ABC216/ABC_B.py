N = int(input())

# A = [int(x) for x in input().split()]

names = set()
ans = "No"
for i in range(N):
    a,b=(str(x) for x in input().split())
    concat_name = a+"+"+b

    if concat_name in names:
        ans = "Yes"
        break
    else:
        names.add(concat_name)

print(ans)