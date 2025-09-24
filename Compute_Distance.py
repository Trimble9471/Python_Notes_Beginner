#Find the distance between two points

#Import the turtle module
from turtle import *

#Prompt the user for the x and y coordinates for two points
x1 = float(input("Enter x coordinate for point 1: "))
y1 = float(input("Enter y coordinate for point 1: "))
x2 = float(input("Enter x coordinate for point 2: "))
y2 = float(input("Enter y coordinate for point 2 : "))

#Compute the distance
distance = ((x2 -x1) ** 2 + (y2 - y1) ** 2) ** 0.5

#Display rqo points and connecting line
penup()
goto(x1,y1) #Location of point 1
pendown()
dot(10, "red")
write("Point 1", font=("Times",14))
goto(x2,y2) #Location of point 2
dot(10, "purple")
write("Point 2", font=("Times",14))

#Move to center of line
penup()
goto((x1 + x2) / 2, (y1 + y2) / 2)
write(distance, font=("Times",14))
hideturtle()
