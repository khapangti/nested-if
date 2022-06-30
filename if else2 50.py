month=input("enter month")
day=int(input("enter day"))
if month=="december" or month=="january" or month=="febuary" and day<=28:
    if day>=1 and day<=31:
        print("winter")
    else:
        print("not winter")
elif month=="march" or month=="april" and day<=30 or month=="may":
    if day>=1 and day<=31:
        print("spring")
    else:
        print("not spring")
elif month=="june" and day<=30 or month=="july" or month=="august":
    if day>=1 and day<=31:
        print("summer")
    else:
        print("not summer")
elif month=="september" and day<=30 or month=="october" or month=="november":
    if day>=1 and day<=31:
        print("autumn")
    else:
        print("not autumn")
else:
    print("not available")
