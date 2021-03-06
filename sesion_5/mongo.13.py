# _*_ coding: utf-8 _*_

from pymongo import MongoClient

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

print  "Coincidencias:", cursor.count()

for persona in cursor:
    print "%s %s (%d)" % (
            persona["nombre"],
            persona["apellido"], 
            persona["edad"]
        )
