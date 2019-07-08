import psycopg2

from operation.connector import conn as connector
from operation.selectData import selectFromDB, selectByName

'''
to prevent double names
'''
def employeeNameValidation(employeeName):
    employeeName = str(employeeName)
    try:
        conn = connector()
        dbCursor = conn.cursor()

        statement = "SELECT name FROM company WHERE name='{employeeName}';"
        sqlQuery = statement.format(employeeName=employeeName)
        dbCursor.execute(sqlQuery)
        checkName = dbCursor.fetchone()

        if(checkName is not None):
            print('Employee Name Has Already In Database\n')
            selectByName(employeeName)
            return True

        else :
            print('Employee Name Is Not Avaible In Database !!!')
            print('Employee Profile Input Can Be Proceed ......')
            print('Please Input Age, Address, and Salary Employee Below...')
            return False
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
