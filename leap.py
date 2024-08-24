doa=input('enter the anniversary date(dd/mm/yyyy): ')
a=int(doa[6:10])
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("Given anniversary year: leap year")
        else:
            print("Given anniversary year: non leap year")
    else:
        print("Given anniversary year: leap year")
else:
    print("Given anniversary year: non leap year")
