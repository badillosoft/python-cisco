# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

personas = db.personas

f = open("personas_nombres.txt", "w")

for persona in personas.find():
    nombre = "%s %s\n" % (persona["nombre"], persona["apellido"])
    f.write(nombre)

f.close()