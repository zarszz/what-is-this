import psycopg2

from operation.connector import conn as connector
from operation.selectData import selectFromDB

'''
to prevent double names
'''
def validationData(employeeName):
    employeeName = str(employeeName)
    try:
        conn = connector()
        dbCursor = conn.cursor()

        statement = "SELECT name FROM company WHERE name='{employeeName}';"
        sqlQuery = statement.format(employeeName=employeeName.lower)
        dbCursor.execute(sqlQuery)
        checkName = dbCursor.fetchone()

        if(checkName is not None):
            print('employee name has already in database')
            print('Name = ', employeeName.capitalize())

        else :
            print('employee name is avaible !!!')

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)