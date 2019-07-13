import psycopg2

from operation.connector import conn as connector
from operation.validation.userValidation import employeeNameValidation
from errorMessage.employeeProfileException import NameHasAvaible


def create_data_to_db(rownumber):
    try:
        conn = connector()
        dbCursor = conn.cursor()
        employeeName = str(input("Enter Employee Name : "))
        EmployeeNameAvaible = employeeNameValidation(employeeName)

        if EmployeeNameAvaible is not True:
            employee_age = str(input("Enter Employee Age : "))
            employee_address = str(input("Enter Employee Address : "))
            employee_salary = float(input("Enter Employee Salary : "))
            employee_db_id = rownumber + 1
            sql = str(
                "INSERT INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES({employee_db_id}, '{employeeName}', {employee_age}, '{employee_address}', {employee_salary}) RETURNING id;")
            sqlQuery = sql.format(employee_db_id=str(employee_db_id),
                                  employeeName=str(employeeName),
                                  employee_age=employee_age,
                                  employee_address=str(employee_address),
                                  employee_salary=str(employee_salary))
            dbCursor.execute(sqlQuery)
            conn.commit()
            print("OPERATION SUCCESSFULLY......")
        elif EmployeeNameAvaible is True:
            raise NameHasAvaible
        dbCursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
