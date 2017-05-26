# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

personas = db.personas

# $gt >
# $gte >=
# $lt <
# $lte <=
# $eq ==
# $ne <>

cursor = personas.find({
    "nombre": "Ana",
    "edad": { "$ne": 44 }
})

for persona in cursor:
    print "%s %s (%d)" % (
            persona["nombre"],
            persona["apellido"], 
            persona["edad"]
        )
