num1=int(input("enter first number pleas: "))
num2=int(input("enter first number pleas: "))
num3=int(input("enter first number pleas: "))
if num1>(num2 or num3):
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)


