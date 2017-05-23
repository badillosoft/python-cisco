# _*_ coding: utf-8 _*_

# * Conocer el lenguaje
# * Resolver el problema en un algoritmo
# * Conocer las librerías

# * Declarar una variable
# * Crear expresiones matemáticas y lógicas
# * Crear condiciones simples (if) dobles (if-else) en cascada (if-elif-else)
# * Recorrer secuencias numéricas. Ejemplo: 1, 2, 3, ..., N 10, 12, 14, ..., N
# * Crear listas
# * Agregar y quitar elementos de una lista
# * Obtener elementos y modificar elementos de una lista por índices
# * Recorrer elementos de una lista por elemento y por índice
# * Crear un ciclo indeterminado
# * Empaquetar y desempaquetar tuplas
# * Guardar datos en un diccionario
# * Recuperar datos de un diccionario
# * Crear funciones
# * Utilizar funciones ya programadas

# * Crear módulos
# * Importar y utilizar módulos
# * Controlar y generar excepciones
# * Escribir archivos
# * Recuperar datos de archivos
# * Crear clases y dominar la POO (constructor, herencia, polimorfismo, encapsulamiento)

# 1. Generar una cadena con el formato
# "<x> <y> <z>" para x, y, z aleatorios en el intervalo [-10, 10]
# Nota: Usar random.uniform(...)

import random

x = random.uniform(-10, 10)
y = random.uniform(-10, 10)
z = random.uniform(-10, 10)

s = "%f %f %f" % (x, y, z)

# 2. Encapsular el código para el paso 1 en la función
# llamada random_point3()

def random_point3():
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    z = random.uniform(-10, 10)

    s = "%.2f %.2f %.2f" % (x, y, z)

    return s


# 3. Generar 100 puntos aleatorios y guardarlos uno por uno
# en el archivo llamado rp3.txt
# Nota: No olvide poner cada punto formateado en una linea
# independiente

f = open("rp3.txt", "w")

for i in range(100):
    p = random_point3()
    f.write("%s\n" % p)

f.close()