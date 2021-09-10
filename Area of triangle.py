import turtle
import math


x1, y1 = eval(input("Enter two coordinates of point 1: "))
x2, y2 = eval(input("Enter two coordinates of point 2: "))
x3, y3 = eval(input("Enter two coordinates of point 3: "))

turtle.showturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.write("Point 1")
turtle.goto(x2, y2)
turtle.write("Point 2")
turtle.goto(x3, y3)
turtle.write("Point 3")
turtle.goto(x1, y1)

turtle.penup()
turtle.goto(-100, -20)
side1 = math.sqrt(((x2 - x1) * (x2 - x1)) + ((y2 - y1) * (y2 - y1)))
side2 = math.sqrt(((x3 - x2) * (x3 - x2)) + ((y3 - y2) * (y3 - y2)))
side3 = math.sqrt(((x3 - x1) * (x3 - x1)) + ((y3 - y1) * (y3 - y1)))

s = (side1 + side2 + side3) / 2

area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

turtle.write(format(area, "10.2f"))

turtle.hideturtle()
