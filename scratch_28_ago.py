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



print ("Crear array con unos")
print (np.ones((2,3,4)))


data = np.array([[ 10, 23,  1,  4,  5],
                [2, 12,  5, 22, 14],
                [2, 10, 5, 24, 10]])

print(data[1:3,2:4])