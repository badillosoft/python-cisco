# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

personas = db.personas

cursor = personas.find({
    "nombre": "Ana",
    "edad": 44
})

for persona in cursor:
    print "%s %s (%d)" % (
            persona["nombre"],
            persona["apellido"], 
            persona["edad"]
        )
