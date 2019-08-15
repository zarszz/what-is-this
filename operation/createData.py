import psycopg2

from operation.connector import conn as connector
from operation.validation.userValidation import(
    employeeNameValidation as employee_name_validation)


def create_data_to_db(row_number):
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

            sql_statement = str(
                "INSERT INTO company (ID,NAME,AGE,ADDRESS,SALARY) " +
                "VALUES(" +
                "{employee_db_id}, '{employee_name}', {employee_age}, " +
                "'{employee_address}', {employee_salary});")

            sql_query = sql_statement.format(employee_db_id=employee_db_id,
                                             employee_name=str(employee_name),
                                             employee_age=employee_age,
                                             employee_address=str(
                                                 employee_address),
                                             employee_salary=str(
                                                 employee_salary))
            db_cursor.execute(sql_query)
            conn.commit()
            print("OPERATION SUCCESSFULLY......")
        if employee_name_status is True:
            print('\n')
            print('\t EMPLOYEE IS AVAIBLE IN DATABASE \t')

        db_cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
