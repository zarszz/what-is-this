import psycopg2

from operation.connector import conn as connector
from operation.validation.userValidation import employeeNameValidation
from errorMessage.employeeProfileException import NameHasAvaible

def create_data_to_db(rownumber):
    employeeId = None
    try:
        conn = connector()
        dbCursor = conn.cursor()
        employeeName = str(input("Enter Employee Name : "))
        EmployeeNameAvaible = employeeNameValidation(employeeName)

        if(EmployeeNameAvaible == False):
            
            employee_age = str(input("Enter Employee Age : "))
            employee_address = str(input("Enter Employee Address : "))
            employee_salart = float(input("Enter Employee Salary : "))
            employee_db_id = rownumber + 1
            sql = str("INSERT INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES({employee_db_id}, '{employeeName}', {employee_age}, '{employee_address}', {employee_salart}) RETURNING id;")
            sqlQuery = sql.format(employee_db_id=str(employee_db_id), employeeName=str(employeeName),
                                employee_age=employee_age, employee_address=str(employee_address), employee_salart=str(employee_salart))

            dbCursor.execute(sqlQuery)
            conn.commit()
            print("OPERATION SUCCESSFULLY......")
        elif(EmployeeNameAvaible == False):
            raise NameHasAvaible
        dbCursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
