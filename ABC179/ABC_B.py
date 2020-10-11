N = int(input())

cnt = 0
ok = 0
flag = True

while cnt < N:
    D1, D2 = (int(x) for x in input().split())
    if D1 == D2:
        ok += 1
        if ok > 2:
            flag = False 
    elif D1 != D2 and flag:
        ok = 0
    cnt += 1
    
if ok > 2:
    print("Yes")
else:
    print("No")