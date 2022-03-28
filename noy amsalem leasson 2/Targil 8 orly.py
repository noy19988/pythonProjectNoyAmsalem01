num=int(input("enter number pleas: "))
digit1=num%10
digit2=num//10
if 0<=num<=99:
    if (digit1==7 or digit2==7) or (num%7==0):
        print("lucky number")
else:
    print("invalid")
