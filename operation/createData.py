from os import system
import psycopg2

from operation.connector import conn as connector
from operation.validation.userValidation import(
                          employeeNameValidation as employee_name_validation)
from statement.sqlmainstatement import get_insert_data_statement


def create_data_to_db(row_number):
    system('clear')
    print('\t INSERT DATA \t\n')
    try:
        conn = connector()
        db_cursor = conn.cursor()
        employee_name = str(input("Enter Employee Name : "))
        employee_name_status = employee_name_validation(employee_name)

        if employee_name_status is not True:
            employee_age = int(input("Enter Employee Age : "))
            employee_address = str(input("Enter Employee Address : "))
            employee_salary = float(input("Enter Employee Salary : "))
            employee_db_id = row_number + 1
            db_cursor.execute(get_insert_data_statement(employee_db_id,
                                                        employee_name,
                                                        employee_age,
                                                        employee_address,
                                                        employee_salary))
            conn.commit()
            print("OPERATION SUCCESSFULLY......")
        if employee_name_status is True:
            print('\n')
            print('\t EMPLOYEE IS AVAIBLE IN DATABASE \t')

        db_cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
