num1=int(input("enter number: "))
while 100<=num1<=999:
    rig=num1%10
    mid=num1%100//10
    lef=num1//100
    print(lef+mid+rig)
    num1=int(input("enter number: "))
print ("not 3 digits")





