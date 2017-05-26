# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

personas = db.personas

query = {
    "nombre": "Ana"
}

personas.delete_many(query)