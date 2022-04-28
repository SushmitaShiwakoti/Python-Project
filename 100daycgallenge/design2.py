import turtle
t= turtle.Turtle()
s= turtle.Screen()
t.speed(0)
s.bgcolor("black")

for i in range(240):
    t.color("aqua")
    t.circle(i*0.6)
    t.color("white")
    t.circle(i*0.4)
    t.right(3)
    t.forward(3)
t.hideturtle()
turtle.done()