p=float(input("enter th prnciple amount: "))
r=float(input("rate of interest in decimal: "))
t=float(input("time(no. of years): "))
si=(p*r*t)/100
print("simple interest rate is: ",si)
a=(p(1+(r/100))**t)
print("compound interest rate is: ",a)
