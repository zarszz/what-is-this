import psycopg2

from operation.connector import conn as connector

'''
to prevent double names
'''


def employeeNameValidation(employee_name, select_specific=False):
    employee_name = str(employee_name)
    try:
        conn = connector()
        db_cursor = conn.cursor()

        statement = "SELECT name FROM company WHERE name='{employee_name}';"
        sql_query = statement.format(employee_name=employee_name)
        db_cursor.execute(sql_query)
        check_name = db_cursor.fetchone()

        if(check_name is not None):
            print('Employee Already In Database !!!\n')
            if (select_specific is False):
                select_by_name(employee_name)
            return True

        else:
            print('Employee Name Is Not Avaible In Database !!!')
            return False
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
