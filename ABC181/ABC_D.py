from collections import Counter
 
n = input()
flag = False
if len(n) <= 2:
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        flag = True
else:
    cnt = Counter(n)
    for i in range(104, 1000, 8):
        if not Counter(str(i)) - cnt:
            flag = True
if flag:
    print("Yes")
else:
    print("No")
