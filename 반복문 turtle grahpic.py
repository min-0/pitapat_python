import turtle

t = turtle.Turtle()
t.hideturtle()

for i in range(5):
    for k in range(5):
        t.left(72)
        t.forward(50)
    t.left(72*2)
