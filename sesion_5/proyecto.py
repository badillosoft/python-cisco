# _*_ coding: utf-8 _*_

from flask import Flask, request
from pymongo import MongoClient

client = MongoClient()
db = client.cisco
personas = db.personas

app = Flask(__name__)

@app.route("/nueva/persona")
def foo():
    nombre = request.args.get("nombre", "Anónimo")
    apellido = request.args.get("apellido", "Ningúno")
    edad = int(request.args.get("edad", "0"))
    sexo = request.args.get("sexo", "No defino")

    cursor = personas.find({
        "nombre": nombre,
        "apellido": apellido
    })

    if cursor.count() > 0:
        # MODIFICAR PERSONA
        return "YA EXISTE D:"

    persona = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "sexo": sexo
    }

    personas.insert_one(persona)

    return "OK"

app.run()