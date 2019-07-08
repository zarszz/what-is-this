import psycopg2

from operation.connector import conn
from operation.validation.userValidation import employeeNameValidation

def deleteData(employeeName):
    try:
        connect = conn()
        dbCursor = connect.cursor()
       
        print("Are you sure want to delete ",employeeName, " profile ??(y/n) -> ", end='')
        deleteChoice = str(input())
                
        if(deleteChoice == "y" or deleteChoice == "Y"):
            sqlStatement = "DELETE FROM company WHERE name='{employeeName}';" 
            sqlQuery = sqlStatement.format(employeeName=employeeName)
        
            dbCursor.execute(sqlQuery)
            connect.commit()
        else:
            print("Aborted To Delete ",employeeName, " Profile")

        dbCursor.close()
        print('OPERATION SUCCESSFULLY . . . . . . .')
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    except(Exception, psycopg2.DataError) as error:
        print(error)

def deleteDataMain():

    employeeName = str(input('Enter Employee Name : '))
    employeeProfileStatus = employeeNameValidation(employeeName)
    
    if employeeProfileStatus is True:
        deleteData(employeeName)
    elif employeeNameValidation is False:
        pass

    
