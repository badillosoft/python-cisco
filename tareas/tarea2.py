# _*_ coding: utf-8 _*_

# Incrementar en una unidad el último
# elemento de una lista

a = [1, 2, 9]

a[-1] += 1

# Si es 10 volver cero el último elemento 
# en incrementar el anterior

if a[-1] == 10:
    a[-1] = 0
    a[-2] += 1

# Generalizar ese método hasta llegar al
# principio si llegara a suceder

def contador(lista):
    v = len(lista) - 1

    while v >= 0:
        lista[v] += 1

        if lista[v] == 10:
            lista[v] = 0
            v -= 1
        else:
            break

    if v < 0:
        print "reset"
        lista.insert(0, 1)

    return lista

print contador([9, 9, 9, 9])