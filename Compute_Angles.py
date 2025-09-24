#Given 3 points of a triangle compute its angles

#Import math and turtle
import math
from turtle import *

#Prompt the user to enter values for 3 points
x1 = float(input("Enter x coordinate for Point 1: "))
y1 = float(input("Enter y coordinate for Point 1: "))
x2 = float(input("Enter x coordinate for Point 2: "))
y2 = float(input("Enter y coordinate for Point 2: "))
x3 = float(input("Enter x coordinate for Point 3: "))
y3 = float(input("Enter y coordinate for Point 3: "))

#Compute the distance between the points
#math.hypot (hypotenuse of a right-angled triangle)
a = math.hypot(x2 - x3, y2 - y3)
b = math.hypot(x1 - x3, y1 - y3)
c = math.hypot(x1 - x2, y1 - y2)

#Compute the angles
A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

#Display the results
print("The three angles are", round(A,2), round(B,2), round(C,2))
#print(f"The three angles are {round(A,2)}, {round(B,2)}

#Goto the first point
penup()
goto(x1,y1)
pendown()
dot(8,"blue")

#Goto point 2
goto(x2,y2)
write(B)
dot(8,"red")

#Goto point 3
goto(x3,y3)
write(C)
dot(8,"orange")

#Goto point 1
goto(x1,y1)
write(A)
hideturtle()
