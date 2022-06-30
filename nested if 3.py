exp_date=int(input("enter expected date"))
exp_month=int(input("enter expected month"))
exp_year=int(input("enter expected year"))
return_date=int(input("enter return_date"))
return_month=int(input("enter return_month"))
return_year=int(input("enter return_year"))
if return_month==exp_month and return_year==exp_year:
    if return_date<=exp_date:
        print("no fine")
    elif return_date>=exp_date:
        n_d_late=exp_date-return_date
        fine=15*n_d_late
        print("fine",fine)
elif return_month>=exp_month and return_year==exp_year:
    if return_date>=exp_date:
        n_d_late=(exp_month-return_month)
        fine=500*n_d_late
        print("fine",fine)
    else:
        print("fine charged")
elif return_month<=exp_month and return_year!=exp_year:
    if return_date>=exp_date:
        fixed_fine=10000
        print("fixed fine")
    else:
        print("no fixed fine")