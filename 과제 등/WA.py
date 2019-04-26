import turtle

t = turtle.Pen()
t.pencolor("red")
t.pensize(2)
t.speed(3)

for i in range(0,20):
    t.clone()
    t.forward(30)
    t.right(18)

for i in range(0,40):
    t.clone()
    t.forward(30)
    t.left(9)

