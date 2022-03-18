#N = input()
#a,b=(int(x) for x in input().split())
 
a = [int(x) for x in input().split()]
 
ans = -1
 
for i in range(a[0],a[1]+1):
    if i % a[2] == 0:
        ans = i
        break
 
print(ans)