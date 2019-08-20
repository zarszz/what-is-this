from os import system
import psycopg2

from operation.connector import conn
from operation.validation.userValidation import (
    employeeNameValidation as employee_name_validation)
from statement.sqlmainstatement import get_delete_data_statement


def delete_data(employee_name):

    try:
        connect = conn()
        db_cursor = connect.cursor()
        print("Are you sure want to delete ", employee_name,
              " profile ??(y/n) -> ", end='')
        delete_choice = str(input())
        if delete_choice in ('y', 'Y'):
            sql_query = get_delete_data_statement(employee_name)
            db_cursor.execute(sql_query)
            connect.commit()
            print('OPERATION SUCCESSFULLY . . . .')
        else:
            print("Aborted To Delete ", employee_name, " Profile")

        db_cursor.close()
        connect.close()
    except(psycopg2.DatabaseError) as error:
        print(error)
    except(psycopg2.DataError) as error:
        print(error)


def delete_data_main():
    system('clear')
    print('\t DELETE DATA MENU \t\n')
    employee_name = str(input('Enter Employee Name : '))
    employee_profile_status = employee_name_validation(employee_name)
    if employee_profile_status is True:
        delete_data(employee_name)
