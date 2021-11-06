S = input()

set_S = set(list(S))
if len(set_S) == 3:
    print(6)
elif len(set_S) == 2:
    print(3)
else:
    print(1)