import numpy as np
from numpy import genfromtxt

datos = genfromtxt('distanciaCombustible.csv', delimiter=',')

dcalculo = datos[1:,2:4]
#distancia = dcalculo[:,0]

print("Maximo Distancia")
print(np.max(dcalculo[:,0]))
print("Maximo Combustible")
print(np.max(dcalculo[:,1]))
print("Minimo Distancia")
print(np.min(dcalculo[:,0]))
print("Minimo Combustible")
print(np.min(dcalculo[:,1]))
print("Promedio Distancia")
print(np.mean(dcalculo[:,0]))
print("Promedio Combustible")
print(np.mean(dcalculo[:,1]))
print("Mediana Distancia")
print(np.median(dcalculo[:,0]))
print("Mediana Combustible")
print(np.median(dcalculo[:,1]))
print("Desviacion Distancia")
print(np.std(dcalculo[:,0]))
print("Desviacion Rendimiento")
print(np.std(dcalculo[:,0]/dcalculo[:,1]))
print("Desviacion Combustible")
print(np.std(dcalculo[:,0]/dcalculo[:,1]))

rendimiento = dcalculo[:,0]/dcalculo[:,1]
print("Maximo rendiemiento")
print(np.max(rendimiento))
print("")