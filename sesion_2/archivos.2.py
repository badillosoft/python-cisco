# _*_ coding: utf-8 _*_

f = open("rp3.txt", "r")

puntos = []

for linea in f:
    # Partimos la linea en una lista con el separador espacio
    a = linea.split(" ")
    
    # Recuperamos el valor de x pero como cadena y lo llamamos xs
    xs = a[0]
    # Recuperamos el valor de y pero como cadena y lo llamamos ys
    ys = a[1]
    # Recuperamos el valor de z pero como cadena y lo llamamos zs
    zs = a[2]

    # Convertimos el número xs que esta dado en cadena a un flotante
    x = float(xs)
    # Convertimos el número ys que esta dado en cadena a un flotante
    y = float(ys)
    # Convertimos el número zs que esta dado en cadena a un flotante
    z = float(zs)

    # Creamos una tupla con las variables x, y, z empaquetadas
    t = (x, y, z)

    puntos.append(t)

print puntos

f.close()