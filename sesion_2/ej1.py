# _*_ coding: utf8 _*_

nombres = ["Pepe", "Paco", "Juan", "Pedro", "Raul", "Ana", "Luisa"]

apellidos = ["Juarez", "Benitez", "Camacho", "Escamilla", "Lopez"]

nombres_gen = []

# Llenar la lista nombres_gen con 10 nombres aleatorios con el
# formato "<nombre> <apellido>"

import random

def generar_nombre():
    # PASO 1: Obtener nombre y apellido aleatoriamente

    # Recuperamos los valores de la lista en el índice especificado
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)

    # Damos el formato adecuado
    #nombre_completo = nombre + " " + apellido
    nombre_completo = "%s %s" % (nombre, apellido)

    # Regresamos el nombre generado con el formato adecuado
    return nombre_completo

# Repitimos el bloque 10 veces
for i in range(100):
    # Generamos un nombre aleatorio (completo)
    nombre = generar_nombre()
    # Guardamos el nombre generado en la lista nombres_gen
    nombres_gen.append(nombre)

print nombres_gen