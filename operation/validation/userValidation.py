import psycopg2

from operation.connector import conn as connector
from operation.selectData import select_by_name


'''
to prevent double names
'''
def employeeNameValidation(employeeName, select_specific=False):
    employeeName = str(employeeName)
    try:
        conn = connector()
        dbCursor = conn.cursor()

        statement = "SELECT name FROM company WHERE name='{employeeName}';"
        sqlQuery = statement.format(employeeName=employeeName)
        dbCursor.execute(sqlQuery)
        checkName = dbCursor.fetchone()

        if(checkName is not None):
            print('Employee Already In Database !!!\n')
            if (select_specific is False):
                select_by_name(employeeName)
            return True

        else:
            print('Employee Name Is Not Avaible In Database !!!') 
            return False
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
