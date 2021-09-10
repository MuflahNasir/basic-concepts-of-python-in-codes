import turtle
import math

x1 = 0
y1 = 0
radius = 100
x2, y2 = eval(input("Enter two coordinates for a point: "))

turtle.penup()
turtle.goto(x1, y1 - radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.dot(6, "red")

d = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

turtle.penup()
turtle.goto(-130, -130)

if d <= radius:
    turtle.write("The point (" + str(x2) + " , " + str(y2) + ") is in the circle")

else:
    turtle.write("The point (" + str(x2) + " , " + str(y2) + ") is outside the circle")

turtle.hideturtle()
