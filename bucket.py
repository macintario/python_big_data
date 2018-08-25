dicc = {
    1:[{"Num":1}],
    2:{"Letra1":"A"},
    3:[{"data1":1,
        "data2":2,
        "data3":3,
        "data4":['a', 'b', 'c', 'd', ('tup1', 'tup2')]
        }]
}

print(dicc)
print(dicc[3][0]['data4'][4][0])


import os
import csv


#def cuentaPalabras(doc)
palabras={}
with open(os.path.join('/', 'home', 'aulae1-b6', 'Descargas', 'TodasLasNoticias.csv'), 'r') as entrada:
    filereader = csv.reader(entrada, delimiter = ',')
    for doc in filereader:
        strDoc=' '.join(doc)
        splitDoc = strDoc.split(" ")
        for palabra in splitDoc:
            if palabra not in palabras:
                palabras[palabra] = 1
            else:
                palabras[palabra] += 1

