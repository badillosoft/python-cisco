# _*_ coding: utf-8 _*_

# Contar todos los números multiplos de 5 entre 1 y 2000 usando while

n = 1
c = 0

while n <= 2000:
    if n % 5 == 0 and n % 13 == 0:
        c += 1
    n += 1

# %d enteros
# %f decimales
# %s cadenas
# %4.5f decimales con 4 unidades y 5 decimales 

print "Hay %d multiplos de 5 entre [1, 2000] %s." % (c, "Hola mundo")

import math

print "Pi vale %.11f" % (math.pi)
