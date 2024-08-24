a=float(input("enter a number:"))
b=float(input("enter a number:"))
c=input("enter the arithmetic value:")
if c=='+' :
    d=a+b
    print ("sum of the two numbers is: ", d)
elif c=='-' :
    d=a-b
    print ("difference of the two numbers is: ", d)
elif c=='*' :
    d=a*b
    print ("product of the two numbers is: ", d)
elif c=='/' :
    d=a/b
    print ("divison of the two numbers is: ", d)
else:
    print ("enter a valuable arithmetic operator")


