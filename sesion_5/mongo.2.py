# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

db = client.cisco

productos = db.productos

for producto in productos.find():
    print producto