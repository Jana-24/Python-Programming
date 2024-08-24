def leap(num):
    if int(num)%4==0:
        if int(num)%100==0:
            if int(num)%400==0:
                print(num, " is a leap year")
            else:
                print(num, " is not a leap year")
        else:
            print(num, " is a leap year")
    else:
        print(num," is not a leap year")

def nop(num):
    if int(num)<0:
        print("it is a negative number")
    elif int(num)>0:
        print("it is a positive number")
    else:
        print("neither negative nor positive")

leap(input("enter a year: "))
nop(input("enter a number: "))
