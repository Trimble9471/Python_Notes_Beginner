#Description: Usefull Turtle functions

#import Turtle
from turtle import *

#Draw line from point 1 to point 2
def drawLine(x1, y1, x2, y2):
    penup()
    goto(x1,y1)
    dot(10,"red")
    pendown()
    goto(x2,y2)
    dot(10,"red")

#Write text at specified location
def writeText(s,x,y):
    penup()
    goto(x,y)
    pendown()
    write(s,font="Times,18,Bold")

#Draw a point at a specified location
def drawPoint(x,y):
    penup()
    goto(x,y)
    pendown()
    dot(13,"blue")

#Draw a circle at centered x,y with teh specified radius
def drawCircle(x,y,radius):
    penup()
    goto(x,y - radius)
    pendown()
    circle(radius)

#Draw a rectangle at x,y with the specified width and height
def drawRectangle(x,y,width,height):
    penup()
    goto(x + width / 2, y + height / 2)
    pendown()
    right(90)
    forward(height)
    right(90)
    forward(width)
    right(90)
    forward(height)
    right(90)
    forward(width)
    
