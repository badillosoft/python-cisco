# _*_ coding: utf-8 _*_

class Calculadora:
    # Definición de métodos (especiales)

    def foo(self):
        print "Hola mundo"
        return 2

a = Calculadora()
b = Calculadora()
c = Calculadora()

r = a.foo()

print r

b.foo()
c.foo()