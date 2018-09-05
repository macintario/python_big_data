import mysql.connector
from mysql.connector import errorcode


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)



config = {
  'user': 'root',
  'password': 'Cic1234*',
  'host': '127.0.0.1',
# 'database': 'university',
  'raise_on_warnings': True,
  'auth_plugin':'mysql_native_password'
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=True)

DB_NAME = 'example'
TABLES = {}
TABLES['alumnos'] = (
    "CREATE TABLE alumnos ("
    "  alumno_id int(11) NOT NULL,"
    "  Nombre varchar(30) NOT NULL,"
    "  ApellidoP varchar(30) NOT NULL,"
    "  ApellidoM varchar(30) NOT NULL,"
    "  Creditos int(11) NOT NULL,"
    "  PRIMARY KEY (alumno_id)"
    ") ENGINE=InnoDB")

try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

for name, ddl in TABLES.iteritems():
    try:
        print("Creating table {}: ".format(name))
        cursor.execute(ddl)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


add_alumno = ("INSERT INTO alumnos (alumno_id, Nombre, ApellidoP, ApellidoM, Creditos) VALUES (%(alumno_id)s, %(Nombre)s, %(ApellidoP)s, %(ApellidoM)s, %(Creditos)s)")
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
	}
]
for row in range(0,len(data_alumno)):
	cursor.execute(add_alumno,data_alumno[row])
cnx.commit()
query = ("SELECT * from alumnos where alumno_id=1")
cursor.execute(query)
for row in cursor:
	print(row)
update_creditos = ("UPDATE alumnos SET Creditos = %s WHERE alumno_id = %s")
nuevo_credito={
	'Creditos' : 10,
	'alumno_id' : 1
}
cursor.execute(update_creditos,(nuevo_credito['Creditos'],nuevo_credito['alumno_id']))
cnx.commit()
query = ("SELECT * from alumnos where alumno_id=1")
cursor.execute(query)
for row in cursor:
	print(row)
cursor.close()
cnx.close()