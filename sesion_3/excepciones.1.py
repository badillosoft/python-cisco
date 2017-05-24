# _*_ coding: utf-8 _*_

try:
    n = int(raw_input("Dame un número: "))
    c = 1 / n
except ValueError:
    print "El número es inválido"
except ZeroDivisionError:
    print "No tiene recíproco"
else:
    print "Tu número es: ", n
