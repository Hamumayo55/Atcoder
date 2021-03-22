N = input()

if len(N) == 1:
    print(N)
else:
    ans= N.split('.')
    print(int(ans[0]))