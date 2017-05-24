f = open("palabras.txt")

contador = 0

for linea in f:
    for i in range(0, len(linea)):
        if linea[i] == "a":
            contador += 1

print contador