# _*_ coding: utf-8 _*_

# Un módulo es un archivo de python
# que puede ser llamado por otros archivos
# y todas las definiciones y variables
# expuestas en el archivo módulo podrán
# ser utilizadas por los otros programas
# que importen el módulo.

# Ejemplo 1: Se crea un archivo llamado
# a.py que contiende la definición de
# la función foo()
# Existe el archivo b.py que import el módulo
# a.py de las siguientes formas:

# Forma canónica: import a
# > a.foo(...)
# Forma simbólica: import a as x
# > x.foo(...)
# Forma parcial: from a import foo
# > foo(...)

import mod_a

print mod_a.invetir("Hola mundo")
print mod_a.partir2([3, 3, 2, 3, 2, 1])
print mod_a.dot([1, 3, 2], [2, 1, 3])

import mod_a as ma

print ma.invetir([5, 4, 3, 2, 1])
print ma.partir2("hola mundo")
print ma.dot([1, 1], [2, 1])

from mod_a import invetir, partir2, dot

print invetir([x ** 2 for x in range(1, 10)])
print partir2("jeje")
print dot([1, 2, 3], [3, 2, 1])

import badillosoft.math.linearalg as alg

print alg.det_matrix("")