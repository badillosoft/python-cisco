from flask import Flask
import json
import random

personas = []

app = Flask(__name__)

@app.route("/personas")
def hola():
    return json.dumps(personas)

@app.route("/nueva/persona/aleatoria")
def npa():
    nombres = ["Pepe", "Juan", "Ana"]

    persona = {
        "nombre": random.choice(nombres),
        "edad": random.randint(0, 100)
    }

    personas.append(persona)

    return json.dumps(persona)

@app.route("/pepe")
def pepe():
    pepes = []

    for p in personas:
        if p["nombre"] == "Pepe":
            pepes.append(p)

    return json.dumps(pepes) 

app.run(host="10.10.2.95")