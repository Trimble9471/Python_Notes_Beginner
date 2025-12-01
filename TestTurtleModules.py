#Testing the custom turtle module

#Import turtle and custom turtle modules
from turtle import *
from UsefullTurtleFunctions import *


#Adjust the speed
speed(3)

#change the shape
shape("turtle")

#Change pensize
pensize(3)

#invoke the drawline function
drawLine(-50,-50,50,50)

#Invoke the writeText function
writeText("Testing useful Turtle Functions",-50,-60)

#Invoke the drawPoint function
drawPoint(0,0)

#Invoke the circle function
drawCircle(0,0,80)

#Invoke the drawRectangle function
drawRectangle(0,0,60,40)
