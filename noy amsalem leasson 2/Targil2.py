num1=int(input("enter first number pleas: "))
if 100<=num1<=999:
    right = num1 % 10
    middle = num1 % 100 // 10
    left = num1 // 100
    print(right+middle+left)
else:
    print("not 3 digits")