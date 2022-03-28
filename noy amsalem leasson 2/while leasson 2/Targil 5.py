num=int(input("enter number pleas: "))
while 10<=num<=99:
    digit1 = num % 10
    digit2 = num // 10
    if (digit1 == 7 or digit2 == 7) or (num % 7 == 0):
        print("lucky number")
    print("not lucky number")
    num = int(input("enter number pleas: "))
print("not 2 digits")