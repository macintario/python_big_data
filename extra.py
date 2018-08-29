import  csv

with open ('distanciaCombustible.csv') as entradacsv:
    lector=csv.reader(entradacsv, delimiter=',')
    datos=list(lector)
print("Ok")

