N = input()

ans = 'No'

for i in range(10):
    S = '0'*i + N
    if S == S[::-1]:
        ans = 'Yes'
        break
print(ans)


