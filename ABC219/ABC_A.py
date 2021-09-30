N = int(input())
#a,b=(int(x) for x in input().split())

#a = [int(x) for x in input().split()]

if N >= 90:
    print('expert')
elif N < 90 and N >= 70:
    print(90-N)
elif N < 70 and N >= 40:
    print(70-N)
else:
    print(40-N)