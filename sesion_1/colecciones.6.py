# _*_ coding: utf-8 _*_

# Diccionarios

persona = {
    "id": 1,
    "nombre": "Pepe",
    "edad": 45,
    "sexo": "Hombre",
    "email": "pepe@gmail.com",
    "amigos": [3, 10],
    "direccion": {
        "calle": "Av. Simpre viva",
        "no_ext": 123,
        "no_int": "SN",
        "colonia": "Juarez"
    }
}

mensaje: {
    "autor": 1,
    "id": "ABC123123123123123",
    "likes": [3, 10, 203],
    "contenido": "Hola mundo",
}

mensaje = ["ABC123123123123", 1, "Hola mundo", [3, 10, 203]]

print persona["nombre"], persona["email"]

print persona["direccion"]["calle"]
print persona["amigos"][1]

