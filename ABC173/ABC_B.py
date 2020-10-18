N = input()
ac = 0
wa = 0
tle = 0
re = 0

for i in range(int(N)):
    S = input()
    if S == "AC":
        ac += 1
    elif S == "WA":
        wa += 1
    elif S == "TLE":
        tle += 1
    else:
        re += 1

print(f"AC x {str(ac)}")
print(f"WA x {str(wa)}")
print(f"TLE x {str(tle)}")
print(f"RE x {str(re)}")
