import psycopg2

from operation.connector import conn as connector

def selectFromDB():
    try:
        conn = connector()
        dbCursor = conn.cursor()

        dbCursor.execute("SELECT name,age,address,salary FROM company")
        print("The number of row = ", dbCursor.rowcount)
        row = dbCursor.fetchone()

        while row is not None:
            print(row)
            row = dbCursor.fetchone()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("fetch sucess.........")     

def selectByName(employeeName):
    # TODO create name validation
    try:
        conn = connector()
        dbCursor = conn.cursor()

        statement = "SELECT name,address,age FROM company WHERE name={employeeName}"
        sqlQuery = statement.format(employeeName=employeeName)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)