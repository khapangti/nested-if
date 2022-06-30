year=int(input('enter the year'))
if year%4==0:   
    if year%100==0 and year%400==0:
        print("leap and century year")
    elif year%100!=0:
        print("leap year")
    else:
        print("century year")
else:
    print("not leap year")