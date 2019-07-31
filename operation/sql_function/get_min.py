from operation.connector import conn
from statement.sqlmainstatement import get_min_salary_statement

def get_min_salary():
    connector = conn()
    db_cursor = connector.cursor()

    sql_statement = get_min_salary_statement()
    db_cursor.execute(sql_statement)

    min_salary_data = db_cursor.fetchone()

    while min_salary_data is not None:
        print('Name   : ', min_salary_data[0])
        print('Salary : ', min_salary_data[1])
        min_salary_data = db_cursor.fetchone()

    db_cursor.close()
    connector.close()
