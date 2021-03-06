import turtle

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.right(60)
turtle.begin_fill()
turtle.color("red")
turtle.circle(50, steps = 3)
turtle.end_fill()

turtle.penup()
turtle.goto(-200, 70)
turtle.pendown()
turtle.right(75)
turtle.begin_fill()
turtle.color("blue")
turtle.circle(50, steps = 4)
turtle.end_fill()

turtle.penup()
turtle.goto(-50, 90)
turtle.pendown()
turtle.right(45)
turtle.begin_fill()
turtle.color("green")
turtle.circle(50, steps = 5)
turtle.end_fill()

turtle.penup()
turtle.goto(120, 40)
turtle.pendown()
turtle.right(90)
turtle.begin_fill()
turtle.color("orange")
turtle.circle(50, steps = 6)
turtle.end_fill()

turtle.penup()
turtle.goto(220, 0)
turtle.pendown()
turtle.right(67)
turtle.begin_fill()
turtle.color("yellow")
turtle.circle(50, steps = 8)
turtle.end_fill()

turtle.hideturtle()
