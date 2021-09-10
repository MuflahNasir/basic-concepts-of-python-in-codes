import turtle

x1, y1 = eval(input("Enter two coordinates for point 1: "))
x2, y2 = eval(input("Enter two coordinates for point 2: "))
x3, y3 = eval(input("Enter two coordinates for point 3: "))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.dot(6, "black")
turtle.goto(x2, y2)
turtle.dot(6, "black")

turtle.penup()
turtle.goto(x3, y3)
turtle.pendown()
turtle.dot(6, "red")
turtle.penup()
turtle.goto(-100, 200)
turtle.hideturtle()

if (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) > 0:
    turtle.write("P2 is on the left side of the line")

elif (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) == 0:
    turtle.write("P2 is on the same line")

elif (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1) < 0:
    turtle.write("P2 is on the right side of the line")
