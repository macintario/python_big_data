import csv

cuenta=dict()
with open('TodasLasNoticias.csv', 'r') as csvfile:
  fileReader = csv.reader(csvfile, delimiter=',')
  for linea in fileReader:
       for columna in linea:
           for palabras in columna.split(' '):
               for palabra in palabras:
                   if palabra in cuenta:
                       cuenta[palabra]+=1
                   else:
                       cuenta[palabra]=1
print(cuenta)
