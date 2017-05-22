# _*_ coding: utf-8 _*_

a = []

for i in range(1, 101):
    a.append(i ** 2)

print a

# Listas generadas

b = [i ** 2 for i in range(1, 101)]

print b

c = [2 * i for i in range(1, 31)]

print c

X = [1, 8, 14, 27, 34, 99]

# Y = [99, 92, 86, 73, 66, 1]

Y = [100 - x for x in X]

Z = [x ** 2 - 2 * x + 18 for x in Y]

print Z

T = [(x, x ** 2) for x in Z]

print T

T = []

for x in Z:
    T.append((x, x ** 2))

A = ["Rojo", "Azul", "Rojo", "Amarillo"]
B = [1, 2, 1, 5]

#C = [{"Color": "Rojo", "Id": 1}, {"Color": "Azul", "Id": 2}, ...]

C = [{ "Color": c, "Id": i } for c, i in zip(A, B)]

print C

D = [1, 3, 4, 5, 7, 9, 11, 8]

pares = [x for x in D if x % 2 == 0]

print pares