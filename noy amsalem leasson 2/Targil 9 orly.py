day=int(input("enter day please: "))
if day>31 or day<1:
    print("eror1")
    month=int(input("enter month please: "))
    if month>12 or month<1:
    print("eror2")
    year=int(input("enter year please: "))
    if year>2022 or year<1950:
    print("eror3")
    right=year%10
    middle=year%100//10
    if 1<=day<=31 and 1<=month<=12 and 1950<=year<=2022:
    if 10 <= day <= 31 and 10 <= month <= 12 and 1950 <= year <= 2022:
        print(f"{day}/{month}/{middle}{right}")
    if 1<=day<=9 and 1<=month<=9:
        day1=str(day)
        day1="0"+day1
        month1 = str(month)
        month1 = "0" + month1
        print(f"{day1}/{month1}/{middle}{right}")
    if 1 <= day <= 9 and 10 <= month <= 12:
        day1 = str(day)
        day1 = "0" + day1
        print(f"{day1}/{month}/{middle}{right}")
    if 10 <= day <= 31 and 1 <= month <= 9:
        month1 = str(month)
        month1 = "0" + month1
        print(f"{day}/{month1}/{middle}{right}")
else:
    print("the date is invalid")

