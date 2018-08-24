import csv
import json
import os
from flask import Flask


with open(os.path.join('/', 'home', 'yan', 'Descargas', 'TodasLasNoticias.csv'), 'r') as entradacsv:
    lector = csv.reader(entradacsv, delimiter=',')
    noticias = list(lector)

listaCategoria = list()
for noticia in noticias:
    if len(noticia) == 5:
        miDicc = dict(fecha = noticia[0], Titulo = noticia[1], Descripcion = noticia[3], Categoria = noticia[4])
        listaCategoria.append(miDicc)

with open('noticias.json', 'w') as archsal:
    json.dump(listaCategoria,archsal)




app = Flask(__name__)


@app.route("/practica_uno/noticias/<nombre>")
def p1_getnews(nombre):
    with open('noticias.json') as jn:
        jsonFile = json.load(jn)

    results = list()
    for record in jsonFile:
        if nombre in record['Categoria']:
            print(record['Categoria'])
            results.append(record)
    return json.dumps(results)

if __name__ == "__main__":
   app.run()
