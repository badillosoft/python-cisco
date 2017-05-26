import turtle
from turtle import Turtle

t1 = Turtle()
t2 = Turtle()

t1.penup()
t1.setpos(100, 100)
t1.pendown()

t1.color("red")
t2.color("blue")

n = 60

t1.fill(True)

for i in range(n):
    t1.forward(10)
    t1.left(360. / n)

    t2.forward(10)
    t2.right(360. / n)

t1.fill(False)

t1.hideturtle()
t2.hideturtle()

turtle.mainloop()