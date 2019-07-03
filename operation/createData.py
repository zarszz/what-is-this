import psycopg2
from operation.connector import conn as connector


def createDataToDB(rownumber):
    employeeId = None
    try:
        conn = connector()
        dbCursor = conn.cursor()
        employeeName = str(input("Enter Employee Name : "))
        employeeAge = str(input("Enter Employee Age : "))
        employeeAddress = str(input("Enter Employee Address : "))
        employeeSalary = float(input("Enter Employee Salary :"))
        employee_db_id = rownumber + 1

        sql = "INSERT INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES({employee_db_id}, '{employeeName}', {employeeAge}, '{employeeAddress}', {employeeSalary}) RETURNING id;"
        sqlQuery = sql.format(employee_db_id=str(employee_db_id), employeeName=employeeName,
                              employeeAge=employeeAge, employeeAddress=employeeAddress, employeeSalary=str(employeeSalary))

        dbCursor.execute(sqlQuery)
        conn.commit()
        dbCursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
        print("INSERT DATA SUCCESSFULLY......")
