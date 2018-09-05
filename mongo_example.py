import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017,username='root',password='Cic1234*',authSource="admin")
db = client["example"]
collection = db["alumnos"]

data_alumno = [
	{
	'alumno_id' : 1,
	'Nombre' : 'Luis',
	'ApellidoP' : 'Hernandez',
	'ApellidoM' : 'Ramirez',
	'Creditos' : 0
	},
	{
	'alumno_id' : 2,
	'Nombre' : 'Jorge',
	'ApellidoP' : 'Guiterrez',
	'ApellidoM' : 'Gonzalez',
	'Creditos' : 2
	},
	{
	'_id' : 2,
	'Nombre' : 'Jorge',
	'ApellidoP' : 'Guiterrez',
	'ApellidoM' : 'Gonzalez',
	'Creditos' : 2
	}
]

docs = collection.insert_many(data_alumno)
print(docs)

docs = collection.find()
for document in docs:
	print(document)

collection.update({"_id" : 2},{"$set" : {"Creditos":10}})
docs = collection.find()
for document in docs:
	print(document)
