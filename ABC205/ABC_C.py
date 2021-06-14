a,b,c=(int(x) for x in input().split())

ans = 0

if c % 2 == 0:
    if abs(a) > abs(b):
        ans = ">"
    elif abs(a) < abs(b):
        ans = "<"
    else:
        ans = "="
else:
    if a > b:
        ans = ">"
    elif a < b:
        ans = "<"
    else:
        ans = "="

print(ans)

