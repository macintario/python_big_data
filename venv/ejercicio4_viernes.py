import os
import csv
import threading
import json

palabras={}

def cuentaPalabras(lista):

    for renglon in lista:
        for columna in renglon:
            columna=columna.split(" ")
            for palabra in columna:
                if palabra not in palabras:
                    palabras[palabra] = 1
                else:
                    palabras[palabra] += 1




with open(os.path.join('/', 'home', 'aulae1-b6', 'Descargas', 'TodasLasNoticias.csv'), 'r') as entrada:
    filereader = csv.reader(entrada, delimiter = ',')
    lisDoc = list(filereader)
tam = len(lisDoc)
espacio = int(tam/4)
lista1 = lisDoc[0:espacio]
lista2 = lisDoc[espacio+1:2*espacio]
lista3 = lisDoc[2*espacio+1:3*espacio]
lista4 = lisDoc[3*espacio+1:]
t1 = threading.Thread(target=cuentaPalabras(lista1), name="t1")
t2 = threading.Thread(target=cuentaPalabras(lista2), name="t2")
t3 = threading.Thread(target=cuentaPalabras(lista3), name="t3")
t4 = threading.Thread(target=cuentaPalabras(lista4), name="t3")

t1.start()
t2.start()
t3.start()
t4.start()

while t1.is_alive() and t2.is_alive() and t3.is_alive() and t4.is_alive():
    sleep(1)
with open("salida_cuenta.json","w") as salida:
    json.dump(palabras,salida)
print(palabras["Nely"])
