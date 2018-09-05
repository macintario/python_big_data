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
 'database': 'my_university',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=True)

DB_NAME = 'example'
TABLES = {}
TABLES['department'] = (
 "  `dept_name` VARCHAR(20) NOT NULL DEFAULT '', "
  " `building` VARCHAR(15) NULL DEFAULT NULL, "
  " `budget` DECIMAL(12,2) NULL DEFAULT NULL, "
  " PRIMARY KEY (`dept_name`))" ""
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


cursor.close()
cnx.close()