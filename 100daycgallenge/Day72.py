import turtle 

pat = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor("Black")
pat.speed(30)

radius = 60
pat.pensize(2)
colour = ['Red', 'magenta', 'Blue']
for x in range(12):

  pat.color(colour[1])
  for i in range(6):
     pat.circle(radius)
     pat.right(60)
  radius = radius + 4

turtle.done()