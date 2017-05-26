# _*_ coding: utf-8 _*_

from pymongo import MongoClient
import pymongo

client = MongoClient()

db = client.cisco

personas = db.personas

cursor = personas.find({
    "$and": [
        { "nombre": { "$in": ["Ana", "Beto"] } },
        { "edad": { "$gte": 20 } },
        { "edad": { "$lte": 30 } },
    ]
})

cursor.sort([
    ("edad", pymongo.DESCENDING),
    ("apellido", pymongo.DESCENDING),
    ("nombre", pymongo.ASCENDING),
])

for persona in cursor:
    print "%s %s (%d)" % (
            persona["nombre"],
            persona["apellido"], 
            persona["edad"]
        )
