import numpy as np
from numpy import genfromtxt
from numpy import arange,array,ones,linalg
from pylab import plot,show

datos = genfromtxt('docentes.csv', delimiter=',')

dcalculo = datos[1:,1:7]
x=dcalculo[:,1]
y=dcalculo[:,2]

A=array([x,ones(np.count_nonzero(x))])

w = linalg.lstsq(A.T, y)[0]

print ("## Coeficientes ##")
print (w)
# plotting the line
line = (w[0]*dcalculo[:,0]+w[1]) # regression line)

print ("Coeficiente de correlación")
print  (np.corrcoef(x,y))


print (line)
plot(x,line,'r-',x,y,'o')
show()