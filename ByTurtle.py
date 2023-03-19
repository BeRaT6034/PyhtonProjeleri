import turtle
turtle.penup()
turtle.goto(-200,0)

for i in range(4):
    turtle.pendown()
    turtle.color("red")
    turtle.forward(100)
    turtle.left(90)
    turtle.speed(1)


turtle.penup()
turtle.goto(50,0)

turtle.pendown()
turtle.color("blue")
turtle.circle(50)
turtle.speed(1)