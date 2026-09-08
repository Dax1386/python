import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle with radius {radius} is: {round(area, 2)}")
#ceil_value = math.ceil(area) round up
#floor_value = math.floor(area) round down

a=float(input("Enter the first number: "))
b=float(input("Enter the second number: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"The length of the hypotenuse is: {round(c, 2)}")