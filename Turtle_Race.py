#Import turtle and random
import turtle,random

#Setup the scree
screen = turtle.Screen()
screen.bgcolor("lightyellow")

#Create a list of turtles
colors = ["red", "blue", "green", "purple", "orange", "pink"]
turtles = []

#Create turtles with random starting positions
for i,color in enumerate(colors):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(-200,100 - i *30)
    turtles.append(t)

#Draw the finish line
finish_line = turtle.Turtle()
finish_line.penup()
finish_line.goto(200,150)
finish_line.pendown()
finish_line.setheading(270)
finish_line.pensize(5)
finish_line.pencolor("black")
finish_line.forward(300)
finish_line.hideturtle()

#Function to move the turtles foward randomly
def move_turtle(t):
    t.forward(random.randint(1,10))

#Race the turtles
while all(t.xcor() < 200 for t in turtles):
    for t in turtles:
        move_turtle(t)

#Determine first and last place turtles
first_place = max(turtles,key = lambda t:t.xcor())
print(f"The First Place Turtle is {first_place.pencolor()} Turtle!")

last_place = min(turtles,key = lambda t:t.xcor())
print(f"The Last Place Turtle is {last_place.pencolor()} Turtle!")
