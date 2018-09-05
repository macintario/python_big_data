####################################################################################
# INSTITUTO POLITECNICO NACIONAL
# CENTRO DE INVESTIGACION EN COMPUTACION
# DIPLOMADO EN DESCUBRIMIENTO DEL CONOCIMIENTO CON
# HERRAMIENTAS BIG DATA
# PRACTICA: PYTHON CON MYSQL
# ALUMNO: IVAN GUTIERREZ RODRIGUEZ
####################################################################################
import mysql.connector
from mysql.connector import errorcode


#
#-------------FUNCION PARA CREACION DE ESQUEMA DE BASE DE DATOS
#
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8mb4'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


#------------------DATOS DE CONEXION DE LA BASE DE DATOS
config = {
    'user': 'root',
    'password': 'Cic1234*',
    'host': '127.0.0.1',
    # 'database': 'my_university',
    'raise_on_warnings': True
}

#---------------------CONEXION CON LA BD
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=True)
# ------------------------NOMBRE DE LA BASE DE DATOS
DB_NAME = 'my_university'

# -------------------DEFINICION DE TABLAS
TABLES = {}
# -----------------------DEPARTMENT
TABLES['department'] = (
    " CREATE TABLE IF NOT EXISTS department ( "
    " dept_name VARCHAR(20) NOT NULL DEFAULT '', "
    " building VARCHAR(15) NULL DEFAULT NULL, "
    " budget DECIMAL(12,2) NULL DEFAULT NULL, "
    " PRIMARY KEY (dept_name) "
    ") ENGINE=InnoDB")
# ----------------------INSTRUCTOR
TABLES['instructor'] = (
    " CREATE TABLE IF NOT EXISTS `instructor` ( "
    " `ID` VARCHAR(5) NOT NULL DEFAULT '', "
    " `name` VARCHAR(20) NOT NULL, "
    " `dept_name` VARCHAR(20) NULL DEFAULT NULL, "
    " `salary` DECIMAL(8,2) NULL DEFAULT NULL, "
    " PRIMARY KEY (`ID`), "
    " INDEX `dept_name` (`dept_name` ASC), "
    " CONSTRAINT `instructor_ibfk_1` "
    " FOREIGN KEY (`dept_name`) "
    " REFERENCES `my_university`.`department` (`dept_name`) "
    ") ENGINE=InnoDB ")
# --------------------STUDENT
TABLES['student'] = (
    "CREATE TABLE IF NOT EXISTS `student` ( "
    "`ID` VARCHAR(5) NOT NULL DEFAULT '', "
    "`name` VARCHAR(20) NOT NULL, "
    "`dept_name` VARCHAR(20) NULL DEFAULT NULL, "
    "`tot_cred` DECIMAL(3,0) NULL DEFAULT NULL, "
    " PRIMARY KEY (`ID`), "
    " INDEX `dept_name` (`dept_name` ASC), "
    " CONSTRAINT `student_ibfk_1` "
    " FOREIGN KEY (`dept_name`) "
    " REFERENCES `department` (`dept_name`)) "
    " ENGINE = InnoDB"
)
# ----------------ADVISOR
TABLES['advisor'] = (
    " CREATE TABLE IF NOT EXISTS `advisor` ( "
    " `s_ID` VARCHAR(5) NOT NULL DEFAULT '', "
    " `i_ID` VARCHAR(5) NULL DEFAULT NULL, "
    " PRIMARY KEY (`s_ID`), "
    " INDEX `i_ID` (`i_ID` ASC), "
    " CONSTRAINT `advisor_ibfk_1` "
    " FOREIGN KEY (`i_ID`) "
    " REFERENCES `instructor` (`ID`) "
    " ON DELETE SET NULL, "
    " CONSTRAINT `advisor_ibfk_2` "
    " FOREIGN KEY (`s_ID`) "
    " REFERENCES `student` (`ID`) "
    " ON DELETE CASCADE) "
    " ENGINE = InnoDB"
)
# ---------------CLASSROOM
TABLES['classroom'] = (
    " CREATE TABLE IF NOT EXISTS `classroom` ( "
    "`building` VARCHAR(15) NOT NULL DEFAULT '', "
    "`room_number` VARCHAR(7) NOT NULL DEFAULT '', "
    "`capacity` DECIMAL(4,0) NULL DEFAULT NULL, "
    " PRIMARY KEY (`building`, `room_number`)) "
    " ENGINE = InnoDB "
)

# SI LA BASE DE DATOS NO EXISTE, LA CREAMOS
try:
    cnx.database = DB_NAME
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# CREACION DE LAS TABLAS
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
# -----------------INSERCION DE DATOS EN LAS TABLAS

# -------------------------DEPARTMENT
add_department = ("INSERT INTO department "
                  " (dept_name, building, budget) "
                  " VALUES (%(dept_name)s, %(building)s, %(budget)s)")

data_department = [
    {
        'dept_name': 'Astronomia',
        'building': 'Erro',
        'budget': 40000
    },
    {
        'dept_name': 'Matematicas',
        'building': 'Leibniz',
        'budget': 80000

    },
    {
        'dept_name': 'Fisica',
        'building': 'Newton',
        'budget': 90000

    }
]
for row in range(0, len(data_department)):
    cursor.execute(add_department, data_department[row])
print("Department")
query = ("SELECT * from department")
cursor.execute(query)
for row in cursor:
    print(row)
# --------------------INSTRUCTOR
add_instructor = ("INSERT INTO instructor "
                  " (ID, name, dept_name, salary) "
                  " VALUES (%(ID)s, %(name)s, %(dept_name)s, %(salary)s)")

data_instructor = [
    {
        'ID': 1,
        'name': 'Ramirez',
        'dept_name': 'Astronomia',
        'salary': 12000
    },
    {
        'ID': 2,
        'name': 'Salinas',
        'dept_name': 'Matematicas',
        'salary': 12000
    },
    {
        'ID': 3,
        'name': 'Andrade',
        'dept_name': 'Fisica',
        'salary': 12000

    }
]
for row in range(0, len(data_instructor)):
    cursor.execute(add_instructor, data_instructor[row])
print("Instructor")
query = ("SELECT * from instructor")
cursor.execute(query)
for row in cursor:
    print(row)
# ----------------------Student
add_student = ("INSERT INTO student "
               " (ID, name, dept_name, tot_cred) "
               " VALUES (%(ID)s, %(name)s, %(dept_name)s, %(tot_cred)s)")

data_student = [
    {
        'ID': 10,
        'name': 'Carlos',
        'dept_name': 'Astronomia',
        'tot_cred': 120
    },
    {
        'ID': 11,
        'name': 'Hugo',
        'dept_name': 'Matematicas',
        'tot_cred': 200
    },
    {
        'ID': 12,
        'name': 'Luis',
        'dept_name': 'Fisica',
        'tot_cred': 150

    }
]
for row in range(0, len(data_instructor)):
    cursor.execute(add_student, data_student[row])
print("Student")
query = ("SELECT * from student")
cursor.execute(query)
for row in cursor:
    print(row)

# ------------------------ADVISOR

add_advisor = ("INSERT INTO advisor "
               " (s_ID, i_ID) "
               " VALUES (%(s_ID)s, %(i_ID)s)")

data_advisor = [
    {
        's_ID': 10,
        'i_ID': 1
    },
    {
        's_ID': 11,
        'i_ID': 2

    },
    {
        's_ID': 12,
        'i_ID': 3

    }
]
for row in range(0, len(data_advisor)):
    cursor.execute(add_advisor, data_advisor[row])
print("Advisor")
query = ("SELECT * from advisor")
cursor.execute(query)
for row in cursor:
    print(row)
# ------------------CLASSROOM

add_classroom = ("INSERT INTO classroom "
                 " (building, room_number, capacity) "
                 " VALUES (%(building)s, %(room_number)s, %(capacity)s)")

data_classroom = [
    {
        'building': 'Leibniz',
        'room_number': '101',
        'capacity': 50
    },
    {
        'building': 'Erro',
        'room_number': '302',
        'capacity': 50
    },
    {
        'building': 'Newton',
        'room_number': '208',
        'capacity': 50
    }
]
for row in range(0, len(data_classroom)):
    cursor.execute(add_classroom, data_classroom[row])
print("Classroom")
query = ("SELECT * from classroom")
cursor.execute(query)
for row in cursor:
    print(row)

# ----- SE CIERRA LA TRANSACCION
cnx.commit()
# -------SE CIERRA EL CURSOR
cursor.close()
# ---SE CIERRA LA CONEXION CON LA BD
cnx.close()
