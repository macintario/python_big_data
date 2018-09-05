####################################################################################
# INSTITUTO POLITECNICO NACIONAL
# CENTRO DE INVESTIGACION EN COMPUTACION
# DIPLOMADO EN DESCUBRIMIENTO DEL CONOCIMIENTO CON
# HERRAMIENTAS BIG DATA
# PRACTICA: PYTHON CON MYSQL
# ALUMNO: IVAN GUTIERREZ RODRIGUEZ
####################################################################################

#importamos la biblioteca para conectarnos a MONGODB
from pymongo import MongoClient

#Nos conectamos a MONGO
#client = MongoClient('localhost', 27017,username='root',password='Cic1234*',authSource="admin")
client = MongoClient('localhost', 27017)
# Usamos la BD test
db = client["test"]
# Seleccionamos la colecccion DATA
collection = db["data"]

# Cargamos los datos
documentos = collection.find()

# Hacemos un diccionario para guardar las cunentas de los documentos
cuenta = dict()

# Iteramos sobre los documentos
for d in documentos:
    campos = d.keys()
#   Iteramos sobre los campos de los documentos
    for c in campos:
        if c in cuenta:
            cuenta[c] += 1
        else:
            cuenta[c] = 1

# Salida de resultados
print("-"*60)
print("Total de documentos:")
print(documentos.count())
print("-"*60)
print("Campos")
for llave,valor in cuenta.items():
    print('%30s' % llave+"     :"+ (str) (valor / documentos.count() * 100) + "%")
print("-"*60)
print("Fin del programa")