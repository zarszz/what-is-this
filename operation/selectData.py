import psycopg2

from operation.connector import conn as connector

def selectFromDB():
    try:
        conn = connector()
        dbCursor = conn.cursor()

        dbCursor.execute("SELECT * FROM company")
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