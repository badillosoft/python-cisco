def invetir(secuencia):
    return secuencia[::-1]

def partir2(lista):
    # lista: [1, 2, 3, 4, 5, 6, 7, 8]
    # cero: [1, 3, 5, 7]
    # uno: [2, 4, 6, 8]

    cero = lista[0::2]
    uno = lista[1::2]
    return (cero, uno)

def dot(u, v):
    s = 0
    for i in range(len(u)):
        s += u[i] * v[i]
    return s