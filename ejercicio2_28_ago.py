import numpy as np
from numpy import genfromtxt
from numpy import arange,array,ones,linalg
from pylab import plot,show

datos = genfromtxt('distanciaCombustible.csv', delimiter=',')

dcalculo = datos[1:,2:4]
#distancia = dcalculo[:,0]

A=array([dcalculo[:,0],ones(np.count_nonzero(dcalculo[:,0]))])

w = linalg.lstsq(A.T, dcalculo[:,1])[0]

print ("## Coeficientes ##")
print (w)
# plotting the line
line = (w[0]*dcalculo[:,0]+w[1]) # regression line)
print("Combustible 100 km")
print(w[0]*100+w[1])
print("Combustible 200 km")
print(w[0]*200+w[1])
print("Combustible 500 km")
print(w[0]*500+w[1])
#Y=mx+b  x=(y-b)/m
print("kilometros con 200 litros")
print((200-w[1])/w[0])

print ("Coeficiente de correlación")
print  (np.corrcoef(dcalculo[:,0],dcalculo[:,1]))


print (line)
plot(dcalculo[:,0],line,'r-',dcalculo[:,0],dcalculo[:,1],'o')
show()