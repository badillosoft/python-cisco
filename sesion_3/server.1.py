from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola():
    return """
    <h1>Hola mundo</h1>
    <input type='text' placeholder='Ingresa un mensaje'>
    <button>enviar</button>
    """

app.run(host="10.10.2.95")