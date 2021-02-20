N = int(input())
# N, A = input().split()

# A = [int(x) for x in input().split()]

if N % 100 == 0:
    print(100)
else:
    print(100 - (N%100))
