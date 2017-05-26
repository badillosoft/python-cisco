from flask import Flask
import json

app = Flask(__name__)

lista = [
    { "x": 123, "a": True, "b": None, "y": "Hola mundo" }
]

@app.route("/hola")
def foo():
    return json.dumps(lista)

app.run()