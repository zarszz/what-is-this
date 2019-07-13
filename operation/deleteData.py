import psycopg2

from operation.connector import conn

from operation.validation.userValidation import (
    employeeNameValidation as employee_name_validation)


def delete_data(employeeName):
    try:
        connect = conn()
        db_cursor = connect.cursor()
        print("Are you sure want to delete ", employeeName,
              " profile ??(y/n) -> ", end='')
        deleteChoice = str(input())
        if (deleteChoice == "y" or deleteChoice == "Y"):
            sql_statement = "DELETE FROM company WHERE name='{employeeName}';"
            sql_query = sql_statement.format(employeeName=employeeName)
            db_cursor.execute(sql_query)
            connect.commit()
            print('OPERATION SUCCESSFULLY . . . .')
        else:
            print("Aborted To Delete ", employeeName, " Profile")

        db_cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    except(Exception, psycopg2.DataError) as error:
        print(error)


def delete_data_main():
    employeeName = str(input('Enter Employee Name : '))
    employeeProfileStatus = employee_name_validation(employeeName)
    if employeeProfileStatus is True:
        delete_data(employeeName)
    elif employee_name_validation is False:
        pass
