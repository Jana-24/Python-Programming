unit=int(input('enter the amount of units consumed: '))
if (0<=unit<=100):
    a=unit*2
    print('the electricity bill is: ', a)
elif (100<unit<=200):
    a=200+((unit-100)*3)
    print('the electricity bill is: ', a)
elif (200<unit<=300):
    a=500+((unit-200)*4)
    print('the electricity bill is: ', a)
elif (300<unit<=400):
    a=900+((unit-300)*5)
    print('the electricity bill is: ', a)
elif (400<unit<=500):
    a=1400+((unit-400)*6)
    print('the electricity bill is: ', a)
elif (500<unit<=600):
    a=2000+((unit-500)*7)
    print('the electricity bill is: ', a)
elif (600<unit<=700):
    a=2700+((unit-600)*8)
    print('the electricity bill is: ', a)
elif (700<unit<=800):
    a=3500+((unit-700)*9)
    print('the electricity bill is: ', a)
else:
    print("enter a valid amount of units")

