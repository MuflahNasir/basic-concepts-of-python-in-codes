import turtle

center1, center2 = eval(input("Enter the center of a circle x, y: "))
radius = eval(input("Enter radius of a circle: "))
point1, point2 = eval(input("Enter points x1, y1: "))

turtle.penup()
turtle.goto(center1, center2 - radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(point1, point2)
turtle.pendown()
turtle.dot(6, "red")

turtle.penup()
turtle.goto(center1 - 70, center2 - radius - 20)
turtle.pendown()

d = ((point1 - center1) * (point1 - center1) + (point2 - center2) * (point2 - center2)) ** 0.5

if d <= radius:

    turtle.write("Point is inside a circle")

else:

    turtle.write("Point is outside a circle")

turtle.hideturtle()

turtle.done()
