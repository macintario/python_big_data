from sklearn import linear_model
from sklearn import preprocessing
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats

print("Leer los datos")
dataPeople = pd.read_csv("clientes.csv")    # Read the data
print("Extraer variable de genero")
genero = dataPeople["Is Female"]
print(genero)
print("Inicializar el modelo de regresion lineal")
log_model = linear_model.LogisticRegression()
print(log_model)
print("Entrenar el modelo")
log_model.fit(X = pd.DataFrame(genero),
              y = dataPeople["Buy"])
print("Revisar la intersección del modelo")
print(log_model.intercept_)
print("Revisar los coeficientes del modelo")
print(log_model.coef_)
print("Realizar la predicción")
preds = log_model.predict(X = pd.DataFrame(genero))
accuracy = log_model.score(X=pd.DataFrame(dataPeople["Is Female"]),
                           y=dataPeople["Buy"])
print("accuracy")
print (accuracy)
train_features = pd.DataFrame([dataPeople["Is Female"],
                              dataPeople["Is Married"],
                              dataPeople["Is Professional"]]).T

print("Caracteristicas de entrenamiento")
print (train_features)
print ("inicializar el modelo")
log_model = linear_model.LogisticRegression()
print("Entrenar el modelo")
log_model.fit(X = train_features ,
             y = dataPeople["Buy"])
print("Intercección ")
print(log_model.intercept_)
print("Coeficientes")
print(log_model.coef_)
print("Realizar predicciones")
preds = log_model.predict(X= train_features)
print("Entrenar el modelo")
log_model.fit(X = train_features ,
             y = dataPeople["Buy"])
print("Intersección ")
print(log_model.intercept_)
print("Coeficientes")
print(log_model.coef_)
print("Realizar predicciones")
preds = log_model.predict(X= train_features)
print("Entrenar el modelo")
log_model.fit(X = train_features ,
             y = dataPeople["Buy"])
print("Intercección ")
print(log_model.intercept_)
print("Coeficientes")
print(log_model.coef_)
print("Realizar predicciones")
preds = log_model.predict(X= train_features)
print("Matriz de confusion")
tablePred=pd.crosstab(preds,dataPeople["Buy"])
print (tablePred)

accuracy  = log_model.score(X=train_features,
                           y=dataPeople["Buy"])
print("accuracy")
print (accuracy)


