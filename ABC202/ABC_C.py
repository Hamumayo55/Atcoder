N = int(input())

num_list = [list(map(int, input().split())) for _ in range(3)]
cnt = 0

for i in range(N):
    if num_list[0][i] in num_list[1]:
        a = num_list[1].index(num_list[0][i])+1
        print([i for i, x in enumerate(num_list[2]) if x == a])
        cnt += len([i for i, x in enumerate(num_list[2]) if x == a])

print(cnt)