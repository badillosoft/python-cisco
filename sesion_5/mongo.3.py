# _*_ coding: utf-8 _*_

from pymongo import MongoClient
import util

client = MongoClient()

db = client.cisco

personas = db.personas

for i in range(100):
    persona = util.random_persona()
    personas.insert_one(persona)

print "Se han creado 100 personas en cisco.personas"