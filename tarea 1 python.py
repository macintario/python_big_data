import pandas as pd


df = pd.read_csv("velocidades.csv")

print(df.describe())
print("Registros:")
print(df.count())
print("Vehiculos:")
print(df['Vehiculo'].unique())
print("Dias Semana")
df['dow'] = pd.to_datetime(df['fecha']).apply(lambda x: x.weekday())
print(df['dow'].unique())
print("Minimo")
fmin=pd.to_datetime(df['fecha']).min()
print(fmin)
print("Maximo")
fmax = pd.to_datetime(df['fecha']).max()
print(fmax)
print("Meses de información")
dif_mon = (fmax.year - fmin.year) * 12 + fmax.month - fmin.month
print(dif_mon)
print("Horario flota")
print(df['hora'].min())
print(df['hora'].max())
print("Velocidad Maxima y vehículo")
vmax = df['velocidad'].max()
print(vmax)
print(df[df['velocidad'] == vmax])
print("Vehiculo s que rebasan los 80 Km/h ")
dfr80 = df[df['velocidad'] > 80]
print(dfr80['Vehiculo'].unique())
print("hora con mayor exceso de velocidad")
df['solohora'] = df['hora'].apply(lambda x: x[:2])
dfmaxvel = df[df['velocidad'] > 80]
print(dfmaxvel.groupby(by=['solohora'] ).count())

