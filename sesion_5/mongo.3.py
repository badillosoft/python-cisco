# _*_ coding: utf-8 _*_

from pymongo import MongoClient

client = MongoClient()

def random_persona():
    persona = {
        "nombre": "...",
        "apellido": "...",
        "edad": 0,
        "sexo": "...",
        "direccion": {
            "calle": "...",
            "numero_int": "..."
            "numero_ext": "...",
            "colonia": "...",
            "codigo_postal": "...",
            "ubicacion": [0, 0]
        }
    }