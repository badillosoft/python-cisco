# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

personas = db.personas

cursor = personas.find({ "nombre": "Ana" })

for persona in cursor:
    print persona["nombre"], persona["sexo"]

query = {
    "nombre": "Ana",
    "sexo": {
        "$ne": "Mujer"
    }
}

update = {
    "$set": {
        "sexo": "Mujer"
    }
}

personas.update_many(query, update)

cursor = personas.find({ "nombre": "Ana" })

print "=" * 50

for persona in cursor:
    print persona["nombre"], persona["sexo"]