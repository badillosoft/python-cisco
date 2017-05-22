# _*_ coding: utf-8 _*_

# Tuplas

t = (1, 5, 8)

# l = list(t)
# t.append(9) # error
# t[0] = 2 # error
# t.pop() # error
# t.*(...) # error

x, y, z = t # Desempaquetar

print x, y, z

def swap(a, b):
    return (b, a)

a, b = swap(1, 2)

c = 8
d = 5

c, d = swap(c, d)

# c, d = (d, c)

def fl(lista):
    return (lista[0], lista[-1])

print fl([1, 2, 3, 4, 5, 6, 7, 8, 9])