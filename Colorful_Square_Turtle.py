#Description: Changing the color of our square spiral

#Import turtle
import turtle

#Set up scree
screen = turtle.Screen()
screen.bgcolor("black")

#Create turtle object
t = turtle.Turtle()
t.shape("turtle")

#Set speed
t.speed(3)

#Create a list of the colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan"]

#Create a for loop
for i in range(50):
    t.pencolor(colors[i % 8]) #Change teh color per iteration
    t.forward(i * 10) #Move foward
    t.left(90)

#Hide turtle
t.hideturtle()
