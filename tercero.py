import os
cuenta = dict()
with open(os.path.join('/', 'home', 'yan', 'Descargas', 'TodasLasNoticias.csv'), 'r') as entrada:
    linea = entrada.readline()
    while linea:
        for palabra in linea.replace(',', ' ').split(" "):
            if palabra in cuenta:
                cuenta[palabra] += 1
            else:
                cuenta[palabra] = 1
print(cuenta)
