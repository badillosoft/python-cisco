import json

f = open("persona.json", "r")

contenido = f.read()

f.close()

persona = json.loads(contenido)
# persona = json.load(f)

print persona