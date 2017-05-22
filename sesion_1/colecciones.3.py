# _*_ coding: utf-8 _*_

# LISTAS

# Perímetro

def dist(x0, y0, x1, y1):
    a = x1 - x0
    b = y1 - y0
    c = (a ** 2 + b ** 2) ** 0.5

    return c

poligono_t = [
    (0, 0),
    (2, 1),
    (1, 2),
    (-1, 1.5),
    (-1, -1)
]

n = len(poligono_t)

p = 0

for i in range(0, n):
    x0, y0 = poligono_t[i]
    x1, y1 = poligono_t[(i + 1) % n]

    print x0, y0
    print x1, y1
    print "-" * 20

    d = dist(x0, y0, x1, y1)

    p += d

print "Prerímetro:", p