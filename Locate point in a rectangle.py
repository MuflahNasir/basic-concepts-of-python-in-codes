import turtle
import math

x, y = 0, 0
h, w = 60, 100

x1, y1 = eval(input("Enter two coordinates of a point: "))

s = turtle.Screen()
turtle.penup()
# start at the center
turtle.goto(x,y)
# head east
turtle.setheading(0)
# go to the middle of the right side
turtle.forward(w / 2)
# turn south, put the pen down, start drawing
turtle.setheading(270)
turtle.pendown()
# southeast corner
turtle.forward(h / 2)
# southwest corner
turtle.setheading(180)
turtle.forward(w)
# northwest corner
turtle.setheading(90)
turtle.forward(h)
# northeast corner
turtle.setheading(0)
turtle.forward(w)
# to the start
turtle.setheading(270)
turtle.forward(h / 2)
turtle.penup()

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.dot(6, "red")

xd = math.sqrt(x1 * x1)
yd = math.sqrt(y1 * y1)

turtle.penup()
turtle.goto(-100, -100)

if (yd <= 2.5) and (xd <= 5.0):
    turtle.write("The point is inside the rectangle")

else:
    turtle.write("The point is outside the rectangle")
    
turtle.hideturtle()
