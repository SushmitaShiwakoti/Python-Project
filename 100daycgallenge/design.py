import turtle
t= turtle.Turtle()
s= turtle.Screen()
t.speed(0)
s.bgcolor("black")
t.hideturtle()
for i in range(40):
    t.left(180)
    t.forward(200)
    t.left(120)
    t.forward(300)
    t.left(3)
    t.pencolor("aque")
t.hideturtle()
turtle.done()