import psycopg2

from operation.connector import conn as connector
from statement.sqlStatement import(
    getSqlStatement as get_sql_statement)

'''
to prevent double names
'''


def employeeNameValidation(employee_name, select_specific=False):
    employee_name = str(employee_name)
    try:
        conn = connector()
        db_cursor = conn.cursor()

        sql_statement = get_sql_statement('get_one_employee_name', None, None, employee_name)
        db_cursor.execute(sql_statement)

        check_name = db_cursor.fetchone()

        if check_name is not None:
            print('Employee is in Database !!!\n')
            if select_specific is False:
                select_by_name(employee_name)
            return True
        else:
            print('Employee Name Is Not Avaible In Database !!!')
            return False
        db_cursor.close()
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def select_by_name(employeeName):
    conn = connector()
    db_cursor = conn.cursor()

    statement = "SELECT name,address,age FROM company " \
                "WHERE name='{employeeName}';"

    sql_query = statement.format(employeeName=employeeName)

    db_cursor.execute(sql_query)
    row_data = db_cursor.fetchone()
    return row_data
