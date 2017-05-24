# _*_ coding: utf-8 _*_

def raiz_cuadrada(x):
    if x < 0:
        raise Exception("El número no puede ser negativo")

    return x ** 0.5

x = float(raw_input("Dame un número: "))

try:
    print raiz_cuadrada(x)
except Exception:
    print "No tiene raíz cuadrada"