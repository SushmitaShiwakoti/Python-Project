import turtle

bob = turtle.Turtle()
bob.speed(10)
bob.color('yellow', 'orange')
bob.begin_fill()
for i in range(10):
   bob.forward(250)
   bob.left(160)

bob.end_fill()   

turtle.done()