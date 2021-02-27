import math
N = int(input())
# N, A = input().split()

# A = [int(x) for x in input().split()]
def pow_r(x, n):
    """
    O(log n)
    """
    if n == 0:  # exit case
        return 1
    if n % 2 == 0:  # standard case ① n is even
        return pow_r(x ** 2, n // 2)
    else:  # standard case ② n is odd
        return x * pow_r(x ** 2, (n - 1) // 2)
        
ard = set()
ans = N

for i in range(2,int(math.sqrt(N))+1):
    if math.log(N,i) >= 2:
        for n in range(2,N):
            if pow_r(i, n) <= N and pow_r(i, n) not in ard:
                ard.add(i**n)
                ans -= 1
            else:
                break
    else:
        break

print(ans)