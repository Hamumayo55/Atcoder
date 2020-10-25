import math
m = int(input())

k = math.log(m, 3)
h = math.log(m, 5)

cnt1 = 0
cnt2 = 0
#print(math.floor(k)+2, math.floor(h)+2)
for i in range(1, math.floor(k)+2):
    #print(i)
    for n in range(1, math.floor(h)+2):
        print(n)
        l = (5**n + 3**i)
        if m == l :
            cnt1 = i
            cnt2 = n
            
if cnt1 == 0 and cnt2 == 0:
    print(-1)
else:
    print(cnt1,cnt2)
