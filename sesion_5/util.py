import random

nombres = [
    "Ana",
    "Beto",
    "Carla",
    "Daniel",
    "Eduardo",
    "Fabian",
    "Gaby",
    "Hugo",
    "Ivan"
]

apellidos = [
    "Alvarez",
    "Benitez",
    "Castillo",
    "Dominguez",
    "Escamilla",
    "Fernandez",
    "Gutierrez",
    "Hernandez",
    "Iglesias"
]

sexos = [
    "Hombre",
    "Mujer",
    "No especificado"
]

calles = [
    "Reforma",
    "Circuito"
]

codigos = [
    "43090",
    "15900",
    "0060"
]

colonias = [
    "Del Valle",
    "Noche Buena",
    "Polanco",
    "Condesa",
    "Roma Norte"
]

def random_persona():
    persona = {
        "nombre": random.choice(nombres),
        "apellido": random.choice(apellidos),
        "edad": random.randint(18, 70),
        "sexo": random.choice(sexos),
        "direccion": {
            "calle": random.choice(calles),
            "numero_int": str(random.randint(1, 1000)),
            "numero_ext": str(random.randint(1, 1000)),
            "colonia": random.choice(colonias),
            "codigo_postal": random.choice(codigos),
            "ubicacion": [
                random.uniform(0, 90),
                random.uniform(-180, 180)
            ]
        },
        "colores": ["rojo", "azul"]
    }

    return persona