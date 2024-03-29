from os import system

from operation.connector import conn
from statement.sqlStatement import getSqlStatement as get_sql_statement


def get_min_salary():
    system('clear')
    print('\t GET MIN SALARY \t\n')
    connector = conn()
    db_cursor = connector.cursor()

    db_cursor.execute(get_sql_statement('min'))

    min_salary_data = db_cursor.fetchall()
    print('\nName   : ', min_salary_data[0][0])
    print('Salary : ', min_salary_data[0][1])
    db_cursor.close()
    connector.close()
