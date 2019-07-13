import psycopg2

from operation.connector import conn

from operation.validation.userValidation import (
    employeeNameValidation as employee_name_validation)


def delete_data(employee_name):
    try:
        connect = conn()
        db_cursor = connect.cursor()
        print("Are you sure want to delete ", employee_name,
              " profile ??(y/n) -> ", end='')
        delete_choice = str(input())
        if delete_choice in ('y', 'Y'):
            sql_statement = "DELETE FROM company WHERE name='{employee_name}';"
            sql_query = sql_statement.format(employee_name=employee_name)
            db_cursor.execute(sql_query)
            connect.commit()
            print('OPERATION SUCCESSFULLY . . . .')
        else:
            print("Aborted To Delete ", employee_name, " Profile")

        db_cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    except(Exception, psycopg2.DataError) as error:
        print(error)


def delete_data_main():
    employee_name = str(input('Enter Employee Name : '))
    employee_profile_status = employee_name_validation(employee_name)
    if employee_profile_status is True:
        delete_data(employee_name)
    elif employee_name_validation is False:
        pass
