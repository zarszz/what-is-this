from operation.connector import conn
from statement.sqlStatement import getSqlStatement as get_sql_statment


def get_max_salary():
    print('\t GET MAX SALARY \t\n')
    connect = conn()
    db_cursor = connect.cursor()
    sql_statement = get_sql_statment('max')
    db_cursor.execute(sql_statement)
    data_result = db_cursor.fetchone()
    i = 1
    while data_result is not None:
        print(i,'\tName : ', data_result[0])
        print('\tSalary: ', data_result[1])
        print()
        data_result = db_cursor.fetchone()
        i = i + 1
    db_cursor.close()
    connect.close()