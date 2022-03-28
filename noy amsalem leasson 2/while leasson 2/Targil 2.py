num1=int(input("enter age: "))
while 0<=num1<=120:
    if 0<=num1<=18:
        print("child")
    if 19 <= num1 <= 60:
        print("adult")
    if 61 <= num1 <= 120:
        print("senior")
    num1 = int(input("enter age: "))
print("invalid age")