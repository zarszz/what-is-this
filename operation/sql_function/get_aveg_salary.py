import os

from operation.connector import conn
from statement.sqlmainstatement import get_average_salary_statement


def get_average_salary():
    os.system('clear')
    print('\t GET AVERAGE SALARY \t\n')
    connector = conn()
    db_cursor = connector.cursor()
    sql_statement = get_average_salary_statement()
    db_cursor.execute(sql_statement)
    aveg_salary = db_cursor.fetchone()
    print('AVERAGE SALARY -> ', aveg_salary[0])
    db_cursor.close()
    connector.close()
