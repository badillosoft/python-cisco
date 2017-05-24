from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola():
    return "Hola cliente CISCO"

app.run(host="10.10.2.95")