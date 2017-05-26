# _*_ coding: utf-8 _*_

class Acumulador:

    def __init__(self):
        self.acumulado = 0

    # x es un parámetro listado
    def agregar(self, *x):
        for e in x:
            self.acumulado += e

a = Acumulador()

print a.acumulado
a.agregar(10, 20, 50, 80)
print a.acumulado
a.agregar(1, 2, 3)
print a.acumulado
a.agregar(1, 2, 3, 4, 5, 6, 7, 8, 9)
print a.acumulado