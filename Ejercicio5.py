import csv
import json
import os
from flask import Flask, jsonify


with open(os.path.join('/', 'vagrant', 'TodasLasNoticias.csv'), 'r') as entradacsv:
    lector = csv.reader(entradacsv, delimiter=',')
    noticias = list(lector)

listaCategoria = list()
for columna in noticias:
    if len(columna) == 5:
        miDicc = dict(fecha = columna[0], Titulo = columna[1], url=columna[2], Descripcion = columna[3], Categoria = columna[4])
        listaCategoria.append(miDicc)

with open('noticias.json', 'w') as archsal:
    json.dump(listaCategoria,archsal)




app = Flask(__name__)


@app.route("/practica_dos/noticias/<nombre>")
def p1_getnews(nombre):
    with open('noticias.json') as jn:
        jsonFile = json.load(jn)

    results = list()
    for record in jsonFile:
        if nombre in record['Categoria']:
            #print(record['Categoria'])
            results.append(record)
    #return json.dumps(results)
    return jsonify(results)

if __name__ == "__main__":
   app.run()
