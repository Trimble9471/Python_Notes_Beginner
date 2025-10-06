#Create different shapes and fill them with color
#using the turtle methods

#import turtle
from turtle import *

#change pensize
pensize(3)

#Change speed
speed(3)

#CHange the shape
shape("turtle")

#Create the shape Triangle
penup()
goto(-170,-25)
pendown()
begin_fill() #Begin to fill color in a shape
color("red")
circle(30, steps = 3) #Draws a triangle
end_fill() #Fill the shape

#Create the shape Square
penup()
goto(-85,-25)
pendown()
begin_fill() #Begin to fill color in a shape
color("blue")
circle(30, steps = 4) #Draws a square
end_fill() #Fill the shape

#Create the Pentagon
penup()
goto(0,-25)
pendown()
begin_fill() #Begin to fill color in a shape
color("green")
circle(30, steps = 5) #Draws a pentagon
end_fill() #Fill the shape

#Create the Hexagon
penup()
goto(85,-25)
pendown()
begin_fill() #Begin to fill color in a shape
color("yellow")
circle(30, steps = 6) #Draws a hexagon
end_fill() #Fill the shape

#Create the Circle
penup()
goto(185,-25)
pendown()
begin_fill() #Begin to fill color in a shape
color("purple")
circle(30) #Draws a circle
end_fill() #Fill the shape

#Title the shapes
color("orange")
penup()
goto(-100,50)
pendown()
write("Cool Colorful SHapes", font=("Times",18,"bold"))
hideturtle()
