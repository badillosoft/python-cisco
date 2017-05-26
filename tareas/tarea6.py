# _*_ coding: utf-8 _*_

f = open("original.txt", "r")

mensaje = f.read()

f.close()

M = 4

subcadenas = []

def siguiente_m(mensaje, i, M):
    return mensaje[i:i + M]

i = 0

while i < len(mensaje) - 4:
    subcadenas.append(siguiente_m(mensaje, i, M))
    i += M

print subcadenas 

def ruleta(cadena, k):
    n = len(cadena)
    return cadena[-k:] + cadena[:n - k]

ruleteadas = []
claves = []

import random

for cadena in subcadenas:
    k = random.randint(1, M - 1)
    claves.append(k)
    ruleteadas.append(ruleta(cadena, k))

print claves
print ruleteadas

encriptado = "".join(ruleteadas)

print encriptado

clave = "%d//" % M

for k in claves:
    clave += "%d:" % k

clave = clave[:-1]

print clave

fe = open("encriptado.txt", "w")

fe.write(encriptado)

fe.close()

fc = open("clave.txt", "w")

fc.write(clave)

fc.close()