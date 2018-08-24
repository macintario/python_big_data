numeros_enteros=[]
for i in range(1, 100000):
    numeros_enteros.append(i)
print(numeros_enteros)

pares=[]
impares=[]
for j in range(1,50000):
    pares.append(2*j)
    impares.append(2*j-1)
miDic=dict(losPares=pares,losImpares=impares)

print(miDic)
print(miDic['losPares'])
print(miDic['losImpares'])


