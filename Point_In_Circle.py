#Determine if a point is inside a circle

#Import the turtle module
from turtle import *

#Prompt user to enter circle coordinates and radius
x1 = float(input("Enter the center x-coordinate of a circle: "))
y1 = float(input("Enter the center y-coordinate of a circle: "))
radius = float(input("Enter the radius of the circle: "))

#Prompt the user to enter the coordinates for the point
x2 = float(input("Enter the point x-coordinate: "))
y2 = float(input("Enter the point y-coordinate: "))

#Draw the circle
penup()
goto(x1,y1 - radius)
pendown()
circle(radius)

#Draw the point
penup()
goto(x2,y2)
pendown()
dot(10,"red")

#Compute the distance
d = (pow(x2 -x1,2) + pow(y2 - y1,2)) ** 0.5

#Display the status
penup()
goto(x1 - 70, y1 - radius - 20)
pendown()

#Using a two-way if, if its in or not
if d <= radius:
    write("The point is inside the circle")
else:
    write("The point is outside the circle")

#Hide the turtle pointer
hideturtle()
