dec=int(input("enter a decimal number: "))
b=''
while dec!=0:
    b=str(dec%2)+b
    dec=int(dec/2)
print(b)
