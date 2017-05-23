# _*_ coding: utf-8 _*_

# Abrimos el archivo rp3.txt en modo lectura
f = open("rp3.txt", "r")

# Lee todas las líneas
lineas = f.readlines()
# Volvemos al principio del archivo
f.seek(0)

# Recorremos línea por línea del archivo
for linea in f:
    print linea

# Cerramos el archivo
f.close()