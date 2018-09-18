import pandas as pd

cars = pd.read_csv("201411.csv")
print(cars.describe())
print(cars.shape)
print(cars.head())
print("Columnas:")
print(cars[:0])
print("Registros:")
print(cars.count())
print("Placas")
print(cars["Placa"].unique())
print("Valores Distintos Placa")
print(len(cars["Placa"].unique()))

print("VIN")
print(cars["VIN"].unique())
print("Valores Distintos VIN")
print(len(cars["VIN"].unique()))

print("Marca")
print(cars["Marca"].unique())
print("Valores Distintos Marca")
print(len(cars["Marca"].unique()))

print("Submarca")
print(cars["Submarca"].unique())
print("Valores Distintos Submarca")
print(len(cars["Submarca"].unique()))


print("Modelo")
print(cars["Modelo"].unique())
print("Valores Distintos Modelo")
print(len(cars["Modelo"].unique()))
print(cars["Modelo"].min())
print(cars["Modelo"].max())


print("CertificadoId")
print(cars["CertificadoId"].unique())
print("Valores Distintos CertificadoId")
print(len(cars["CertificadoId"].unique()))

print("VerificentroId")
print(cars["VerificentroId"].unique())
print("Valores Distintos VerificentroId")
print(len(cars["VerificentroId"].unique()))


print("troId")
print(cars["troId"].unique())
print("Valores Distintos troId")
print(len(cars["troId"].unique()))


print("Fecha")
print(cars["Fecha"].unique())
print("Valores Distintos Fecha")
print(len(cars["Fecha"].unique()))
print("De:"+cars["Fecha"].min()+" hasta:"+cars["Fecha"].max())


print("Hora")
print(cars["Hora"].unique())
print("Valores Distintos Hora")
print(len(cars["Hora"].unique()))
print("De:"+cars["Hora"].min()+" hasta:"+cars["Hora"].max())

print("Resultado")
print(cars["Resultado"].unique())
print("Valores Distintos Resultado")
print(len(cars["Resultado"].unique()))

print("CausaRechazo")
print(cars["CausaRechazo"].unique())
print("Valores Distintos CausaRechazo")
print(len(cars["CausaRechazo"].unique()))

