age=int(input("enter age"))
sex=input("enter M or F")
m_s=input("enter Y or N")
if sex=="M":
    if age>=20 and age<=40 and m_s=="Y":
        print("he may work in anywhere")
    elif age>=40 and age<=60 and m_s=="Y":
        print("he will work in urban areas only")
    else:
        print("error")
elif sex=="F":
    print("she will work only in urban areas")