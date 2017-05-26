# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

personas = db.personas

for persona in personas.find():
    print "%s %s" % (persona["nombre"], persona["apellido"])