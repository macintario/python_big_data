from numpy import arange,array,ones,linalg
from pylab import plot,show

print ("linear regression...")
xi = arange(0,9)

A = array([ xi, ones(9)])
print ("## Matriz A ##")
print (A)
# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]

print ("## Transpuesta de A ##")
print (A.T)
w = linalg.lstsq(A.T,y)[0] # obtaining the parameters

print ("## Coeficientes ##")
print (w)
# plotting the line
line = (w[0]*xi+w[1]) # regression line)

print (line)
plot(xi,line,'r-',xi,y,'o')
show()
