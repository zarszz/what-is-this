import psycopg2

from operation.connector import conn as connector
from operation.selectData import selectByName

from operation.validation.userValidation import employeeNameValidation

from errorMessage.employeeProfileException import NameHasAvaible


def createDataToDB(rownumber):
    employeeId = None
    try:
        conn = connector()
        dbCursor = conn.cursor()
        employeeName = str(input("Enter Employee Name : "))
        EmployeeNameAvaible = employeeNameValidation(employeeName)

        if(EmployeeNameAvaible == False):
            
            employeeAge = str(input("Enter Employee Age : "))
            employeeAddress = str(input("Enter Employee Address : "))
            employeeSalary = float(input("Enter Employee Salary : "))
            employee_db_id = rownumber + 1
            sql = "INSERT INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES({employee_db_id}, '{employeeName}', {employeeAge}, '{employeeAddress}', {employeeSalary}) RETURNING id;"
            sqlQuery = sql.format(employee_db_id=str(employee_db_id), employeeName=str(employeeName),
                                employeeAge=employeeAge, employeeAddress=str(employeeAddress), employeeSalary=str(employeeSalary))

            dbCursor.execute(sqlQuery)
            conn.commit()
            print("OPERATION SUCCESSFULLY......")
        elif(EmployeeNameAvaible == False):
            raise NameHasAvaible
        dbCursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    except NameHasAvaible:
        print("Operation Error : Name has avaible in database")
        print()

def main():
    createDataToDB()
