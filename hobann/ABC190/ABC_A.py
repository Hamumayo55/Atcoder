#N = int(input())
B = [int(x) for x in input().split()]

if B[2] == 0:
    if B[0] > B[1]:
        print("Takahashi")
    else:
        print("Aoki")
else :
    if B[1] > B[0]:
        print("Aoki")
    else:
        print("Takahashi")