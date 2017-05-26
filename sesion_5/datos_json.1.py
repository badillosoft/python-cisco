import json

persona = {
    "nombre": "Fausto",
    "correo": "fausto@email.com",
    "edad": 34,
    "skills": []
}

contenido = json.dumps(persona)

f = open("persona2.json", "w")

f.write(contenido)

f.close()