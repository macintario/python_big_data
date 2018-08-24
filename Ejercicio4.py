import  os
import json
from flask import Flask
from random import random

with open(os.path.join('/', 'home', 'yan', 'Descargas','mexico-transport-current.geojson')) as f:
    datos = json.load(f)
print(datos)
for i in datos['features']:
    print(i['properties'])
    i['properties']['bancos'] = random()
    i['properties']['escuelas'] = random()
    i['properties']['mercados'] = random()
    print(i['properties'])
with open('acesibilidad.geojson', 'w') as archsal:
    json.dump(datos,archsal)

app = Flask(__name__)


@app.route("/practica_uno/geojsonFile")
def p1_getgeojson():
    with open('acesibilidad.geojson') as gj:
        jsonFile = json.load(gj)
    return json.dumps(jsonFile)

if __name__ == "__main__":
   app.run()
