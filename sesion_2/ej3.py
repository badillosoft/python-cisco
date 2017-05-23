# _*_ coding: utf-8 _*_

# Invertir una lista

a = [1, 5, 4, 6, 8, 3, 2]

a.reverse()

print a

b = [1, 3, 5, 7]

print b[1:3]

c = [1, 2, 3, 6, 1, 7, 5, 3, 5, 8]

print c[2:6]

print c[3:]

print c[:6]

print c[::2]

print c[3::2]

print c[7:1:-1]

# lista[i:f:s] [i] [i:f] [i:f:s]
# i - índice donde empiza (si no se define es el primero o último)
# f - índice límite o final (si no se define el último más uno o el primero)
# no toca a f
# s - salto, puede positivo o negativo

bv = [1, 2, 3, 5, 6, 8, 4, 6, 1]

X = bv[0::3]
Y = bv[1::3]
Z = bv[2::3]

# Invertir una palabra

print "Hola"[::-1]

# 1. Abrir el archivo palabras.txt (f)
# 2. Abrir el archivo ipalabras.txt (fi)
# 3. Recorrer cada línea del archivo f
#    3.1 Invertir la línea
#    3.2 Guardar la línea en el archivo fi
# 4. Cerrar el archivo f
# 5. Cerrar el archivo fi