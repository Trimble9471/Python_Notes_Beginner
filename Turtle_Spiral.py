#Description: Create a color changing spiral

#Import turtle module
import turtle

#Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

#Create turtle object
t = turtle.Turtle()
t.shape("turtle")

#Set pen speed
t.speed(0)

#Create a list of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

#Create a for loop to iterate 120 times
for i in range(120):
    t.pencolor(colors[i % 6]) #Change color per iteration
    t.forward(i * 3 / 2 + i) #Move the turtle forward
    t.left(59)

#Hide the turtle
t.hideturtle()
