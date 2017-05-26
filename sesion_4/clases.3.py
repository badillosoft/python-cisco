# _*_ coding: utf-8 _*_

class Pelicula:
    def __init__(self, titulo, autor, anjo):
        self.titulo = titulo
        self.autor = autor
        self.anjo = anjo
        self.resenja = ""

    def descripcion(self):
        print "%s %s (%d)" % (self.titulo, self.autor, self.anjo)

    
p1 = Pelicula("Toy Story", "Pixar", 1994)

p2 = Pelicula("La Montaña Sagrada", "Jodorowsky", 1980)

p1.descripcion()
p1.descripcion()

p2.descripcion()
p2.descripcion()



