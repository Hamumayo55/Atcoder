hon_list = [2,4,5,7,9]


N = input()

if N[len(N)-1] == '3':
    print("bon")
elif int(N[len(N)-1]) in hon_list:
    print("hon")
else:
    print("pon")