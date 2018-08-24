import os
cuenta = dict()

with open(os.path.join('/', 'home', 'yan', 'Descargas', 'TodasLasNoticias.csv'), 'r') as entrada:
    lineas = entrada.readlines()
    for linea in lineas:
        for palabra in linea.replace(',', ' ').split(" "):
            if palabra in cuenta:
                cuenta[palabra] += 1
            else:
                cuenta[palabra] = 1
print(cuenta)
