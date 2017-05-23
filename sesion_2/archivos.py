# _*_ coding: utf-8 _*_

# r - read / lectura
# w - write / escritura
# a - append / continuación
# r+ | w+ - full / lectura+escritura 
# a+ / full append / lectura+escritura+continuación

# rb / wb / ab (archivos binarios)

f = open("datos.txt", "w")

f.write("Hola mundo\n")
f.writelines([
    "Una linea\n",
    "Otra linea"
])

f.close()