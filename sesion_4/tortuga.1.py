import turtle
from turtle import Turtle

class SuperTurtle(Turtle):

    def __init__(self):
        # Llamamos al constructor de la clase Padre (base)
        Turtle.__init__(self)

    def polygon(self, n, distance):
        self.pendown()
        for i in range(n):
            self.forward(distance)
            self.left(360. / n)
        self.penup()

    def chess_board(self):
        self.speed(0)
        for i in range(8):
            for j in range(8):
                self.setpos(j * 10, i * 10)

                if (i + j) % 2 == 0:
                    self.fill(True)

                self.polygon(4, 10)

                self.fill(False)

st1 = SuperTurtle()

st1.chess_board()

turtle.mainloop()