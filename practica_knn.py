import  pandas as pd

#Funcion de normalizacion MIN-MAX
def normaliza_min_max (columna):
    maximo = columna.max()
    minimo = columna.min()
    columna = (columna-minimo+0.)/(maximo-minimo+0.) # Se agrega "0." para evitar división entera
    #print(columna)
    return columna

#Leemos datos de entrenamiento
entrenamiento = pd.read_csv("entrenamiento.csv")
normalizado = entrenamiento
#Normalizamos
normalizado["Precio"]=normaliza_min_max(entrenamiento["Precio"])
normalizado["Metros Cuadrados"]=normaliza_min_max(entrenamiento["Metros Cuadrados"])
normalizado["Baños"]=normaliza_min_max(entrenamiento["Baños"])
normalizado["Cuartos"]=normaliza_min_max(entrenamiento["Cuartos"])
normalizado["Estacionamiento"]=normaliza_min_max(entrenamiento["Estacionamiento"])
normalizado["Mantenimiento"]=normaliza_min_max(entrenamiento["Mantenimiento"])




print("OK")