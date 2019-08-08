from os import system

from operation.connector import conn
from statement.sqlStatement import getSqlStatement as get_sql_statment


def get_max_salary():
    system('clear')
    print('\t\n GET MAX SALARY \t\n')

    connect = conn()
    db_cursor = connect.cursor()

    sql_statement = get_sql_statment('max')
    db_cursor.execute(sql_statement)

    data_result = db_cursor.fetchall()

    for data in enumerate(data_result, start=1):
        print(data[0],'\tName : ', data[1][0])
        print('\tSalary: ', data[1][1])
        print('\n')

    db_cursor.close()
    connect.close()