import turtle

x1 = 0
y1 = 0
x2 = 200
y2 = 0
x3 = 0
y3 = 100

x4, y4 = eval(input("Enter two coordinates of a point: "))

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x1, y1)

turtle.penup()
turtle.goto(x4, y4)
turtle.dot(6, "red")

c1 = (x2 - x1) * (y4 - y1) - (y2 - y1) * (x4 - x1)
c2 = (x3 - x2) * (y4 - y2) - (y3 - y2) * (x4 - x2)
c3 = (x1 - x3) * (y4 - y3) - (y1 - y3) * (x4 - x3)

turtle.penup()
turtle.goto(-300, 200)

if (c1 < 0 and c2 < 0 and c3 < 0) or (c1 > 0 and c2 > 0 and c3 > 0):
    turtle.write("Point is in the triangle")

else:
    turtle.write("Point is outside the triangle")

turtle.hideturtle()
