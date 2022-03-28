name=(input("enter your name please: "))
age=(int(input("enter your age please: ")))
year=(int(input("enter the year please: ")))
newyear=(int(input("enter your desired year in which your age will be calculated: ")))
sumyear=newyear-year
newage=age+sumyear
print (f"{name} will be {newage} years old in {newyear} ")