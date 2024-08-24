inc=int(input('enter your income: '))
if (inc<=150000):
    print('No Tax')
elif (150000<inc<=300000):
    tax=inc*0.1
    print('Tax to be paid is ',tax)
elif (300000<inc<=500000):
    tax=inc*0.2
    print('tax to be paid is ',tax)
elif (500000<inc):
    tax=inc*0.3
    print('tax to be paid is ',tax)
else:
    print('enter a valid income')
