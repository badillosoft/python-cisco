def copy_paste(nombre_o, nombre_d):
    fo = open(nombre_o, "r")
    fd = open(nombre_d, "w")

    for linea in fo:
        fd.write(linea)

    fo.close()
    fd.close()

copy_paste("palabras.txt", "palabras_copia.txt")