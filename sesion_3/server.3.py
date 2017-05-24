from flask import Flask
from flask import request
import json

app = Flask(__name__)

# Test: http://localhost:5000/suma?a=12
@app.route("/suma")
def suma():
     a = int(request.args.get("a", 0))
     b = int(request.args.get("b", 0))

     return str(a + b)

app.run(host="localhost")