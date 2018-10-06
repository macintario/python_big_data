import  pandas as pd
import math

#Funcion de normalizacion MIN-MAX
from pandas import DataFrame


def normaliza_min_max (columna):
    maximo = columna.max()
    minimo = columna.min()
    columna = (columna-minimo+0.)/(maximo-minimo+0.) # Se agrega "0." para evitar división entera
    #print(columna)
    return columna


def normaliza_renglon(renglon,entrenamiento):
    renglon_normalizado = renglon.copy()
    for atributo in entrenamiento:
        if atributo != "Invertir":
            minimo = entrenamiento[atributo].min()+0.
            maximo = entrenamiento[atributo].max()+0.
            valor = renglon[atributo]+0.
            normVal= (valor-minimo)/(maximo-minimo)
            renglon_normalizado[atributo] = normVal
    return renglon_normalizado

def obten_distancias(renglon_normalizado,entrenaminento_normalizado):
    distancias = pd.DataFrame(columns=["Indice","Distancia"])  # type: DataFrame
    dimensiones = entrenaminento_normalizado.columns
    for index, row in entrenaminento_normalizado.iterrows():
        distancia_renglon = 0.
        for atributo in dimensiones:
            if atributo != "Invertir":
                dist_dim = renglon_normalizado[atributo] - row[atributo]
                distancia_renglon += dist_dim*dist_dim
        distancia_renglon = math.sqrt(distancia_renglon)
        distancias.loc[index,"Indice"] = index
        distancias.loc[index, "Distancia"] = distancia_renglon
    return distancias

def clasifica(k, pruebas, normalizado, entrenamiento):
    print("##########################################")
    print("               K=", k)
    for index, renglon in pruebas.iterrows():
        renglon_normalizado = renglon.astype(float)
        renglon_normalizado = normaliza_renglon(renglon_normalizado,entrenamiento)
        distancias = obten_distancias(renglon_normalizado,normalizado)
        distancias = distancias.sort_values( by = 'Distancia',ascending=1)
        si = 0
        no = 0
        for i in range (0, k):
            inversion = entrenamiento.loc[distancias.loc[i,"Indice"],"Invertir"]
            if inversion == "Si":
                si += 1
            else:
                no += 1
            #print(inversion)
        if si > no :
            consejo = "Si"
        else:
            consejo = "No"

        print("**********************************************************")
        print("Instancia ")
        print(renglon)
        print("Consejo:", consejo, " (SI", si, " vs NO", no,")")

################################### INICIO ########################################
#Leemos datos de entrenamiento
entrenamiento = pd.read_csv("entrenamiento.csv")
normalizado = entrenamiento.copy()
#Normalizamos
for columna in entrenamiento:
    if columna != "Invertir":
        normalizado[columna] = normaliza_min_max(normalizado[columna])
print(normalizado)

#leemos los datos a clasificar
prueba = pd.read_csv("prueba.csv")
#efectuamos clasificación para k=1,3,5
for k in 1,3,5:
    clasifica(k,prueba,normalizado,entrenamiento)


print("Fin de la corrida....")