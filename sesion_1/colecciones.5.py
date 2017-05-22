# _*_ coding: utf-8 _*_

# LISTAS

# Perímetro

def dist(x0, y0, x1, y1):
    a = x1 - x0
    b = y1 - y0
    c = (a ** 2 + b ** 2) ** 0.5

    return c

poligono_t = [
    { "x": 0, "y": 0 },
    { "x": 2, "y": 1 },
    { "x": 1, "y": 2 },
    { "x": -1, "y": 1.5 },
    { "x": -1, "y": -1 },
]

n = len(poligono_t)

p = 0

for i in range(0, n):
    dici = poligono_t[i]

    x = dici["x"]
    y = dici["y"]

    print dici

print "Prerímetro:", p