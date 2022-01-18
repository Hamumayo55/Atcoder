n = input()
#a,b=(int(x) for x in input().split())

# A = [int(x) for x in input().split()]
ans = int(n)
ans += int(n[1]+n[2]+n[0])
ans += int(n[2]+n[0]+n[1])

print(ans)
