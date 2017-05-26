# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco
# db = client["cisco"]

productos = db.productos
# productos = db["productos"]

productos.insert_one({
    "nombre": "Instalación de ...",
    "área": "redes",
    "descripción": "Se asignan tantos técnicos bla bla bla"
})

# client.close()