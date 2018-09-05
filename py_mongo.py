import pymongo
from pymongo import MongoClient


#client = MongoClient('localhost', 27017,username='root',password='Cic1234*',authSource="admin")
client = MongoClient('localhost', 27017)
db = client["test"]
collection = db["data"]

documentos = collection.find()

cuenta = dict()

nDocs = documentos.count()
for d in documentos:
    llaves = d.keys()
    for k in llaves:
        if k in cuenta:
            cuenta[k] += 1
        else:
            cuenta[k] = 1

print("Total de documentos")
print(cuenta["_id"])  # Todos los documentos tienen _id

for llave,valor in cuenta.items():
    print("Llave      :" + llave)
    print("  Presencia:" + (str) (valor / cuenta["_id"] * 100) + "%")