# _*_ coding: utf-8 _*_

class Punto:

    def __init__(self, **dic):
        self.x = 0
        self.y = 0

        if dic.has_key("x"):
            self.x = dic["x"]
        
        if dic.has_key("y"):
            self.y = dic["y"]

p1 = Punto()

p2 = Punto(x=1)

p3 = Punto(y=5, x=10)

print p1.x, p1.y
print p2.x, p2.y
print p3.x, p3.y