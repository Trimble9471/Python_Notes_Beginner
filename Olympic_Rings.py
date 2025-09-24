#Aaron Trimble
#7007931350
#Turtle Olympic Rings
#Drawing Olympic rings using Turtle

#import Turtle module
from turtle import *

#increase the pensize
pensize(7)

#change the speed
speed(5)

#Create the Blue ring
color("blue") #changes the color of the turtle pointer
penup() #pulls the pen off the canvas
goto(-110,-25) #moves pen to location
pendown() #puts the pen back on canvas
circle(45) #makes a circle with the given radius

#Create the Black ring
color("black") #changes the color of the turtle pointer
penup() #pulls the pen off the canvas
goto(0,-25) #moves pen to location
pendown() #puts the pen back on canvas
circle(45) #makes a circle with the given radius

#Create the Red ring
color("red") #changes the color of the turtle pointer
penup() #pulls the pen off the canvas
goto(110,-25) #moves pen to location
pendown() #puts the pen back on canvas
circle(45) #makes a circle with the given radius

#Create the Yellow ring
color("yellow") #changes the color of the turtle pointer
penup() #pulls the pen off the canvas
goto(-55,-75) #moves pen to location
pendown() #puts the pen back on canvas
circle(45) #makes a circle with the given radius

#Create the Green ring
color("green") #changes the color of the turtle pointer
penup() #pulls the pen off the canvas
goto(55,-75) #moves pen to location
pendown() #puts the pen back on canvas
circle(45) #makes a circle with the given radius

#Hide turtle pointer
hideturtle()
