import os

from operation.connector import conn
from statement.sqlStatement import get_average_salary

def get_average_salary():
    os.system('clear')
    print('\t GET AVERAGE SALARY \t')
    connector = conn()
    db_cursor = connector.cursor()
    db_cursor.execute(get_average_salary())
    aveg_salary = db_cursor.fetchone()
    print('AVERAGE SALARY -> ', aveg_salary)


