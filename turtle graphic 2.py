import turtle

n = eval(input("정수의 길이는: "))

t = turtle.Turtle()
t.shape('classic')

t.circle(n//2)
t.forward(n//2)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
