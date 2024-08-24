shape= input("enter the shape(circle or triangle) to find the area: ")
if shape == 'circle':
    rad = int(input("enter the radius of the circle: "))
    area = 3.14 * rad ** 2
    print ("area of the circle is: ",area)
elif shape == 'triangle':
    h = float(input("enter the height of the triangle: "))
    b = float(input("enter the base length of the triangle: "))
    area = (b*h)/2
    print ("area of the triangle is: ",area)
else:
    print ("enter proper shape format")

