import  pandas as pd

#Funcion de normalizacion MIN-MAX
def normaliza_min_max (columna):
    maximo = columna.max()
    minimo = columna.min()
    columna = (columna-minimo+0.)/(maximo-minimo+0.) # Se agrega "0." para evitar división entera
    print(columna)
    return columna

#Leemos datos de entrenamiento
entrenamiento = pd.read_csv("entrenamiento.csv")
#Normalizamos
entrenamiento["Precio"]=normaliza_min_max(entrenamiento["Precio"])
entrenamiento["Metros Cuadrados"]=normaliza_min_max(entrenamiento["Metros Cuadrados"])
entrenamiento["Baños"]=normaliza_min_max(entrenamiento["Baños"])
entrenamiento["Cuartos"]=normaliza_min_max(entrenamiento["Cuartos"])
entrenamiento["Estacionamiento"]=normaliza_min_max(entrenamiento["Estacionamiento"])
entrenamiento["Mantenimiento"]=normaliza_min_max(entrenamiento["Mantenimiento"])

''