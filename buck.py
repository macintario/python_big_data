import pandas as pd


df = pd.read_csv("velocidades.csv")

print(df.describe())
print("Registros:")
print(df.count())
print("Vehiculos:")
print(df['Vehiculo'].unique())

print(df.groupby(['velocidad','Vehiculo']).max())
dfr80 = df[df['velocidad'] > 80]
print(dfr80)
print(dfr80.groupby(['fecha','Vehiculo']).max().loc[:,['velocidad']])