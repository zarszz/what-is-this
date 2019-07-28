import os
import psycopg2

from operation.connector import conn as connector
from operation.specific_select import select_specific_by_data


def select_from_db():
    '''
    '''
    try:
        conn = connector()
        db_cursor = conn.cursor()

        db_cursor.execute("SELECT name,age,address,salary FROM company")
        print("The number of row = ", db_cursor.rowcount, "\n")

        row = db_cursor.fetchone()
        i = 1

        while row is not None:
            print(i, '.', row)
            row = db_cursor.fetchone()
            i = i + 1

        db_cursor.close()
        conn.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


def specific_select(choice):
    '''
    '''
    print('\n')
    if choice == '1':
        select_from_db()
    if choice == '2':
        select_specific_by_data('address')
    if choice == '3':
        select_specific_by_data('age')


def select_data_menu():
    '''
    '''
    os.system('clear')
    print('\tSELECT DATA MENU\t\n')
    print('Please Choose Option Below')
    print('1. Select All Data')
    print('2. Select Employee Address')
    print('3. Select Employee Age')
    choice = str(input('Enter Your Choice -> '))
    specific_select(choice)


def select_by_name(employee_name):
    '''
    '''
    try:
        conn = connector()
        db_cursor = conn.cursor()

        statement = "SELECT name,address,age,salary FROM company " \
                    "WHERE name='{employee_name}';"
        sql_query = statement.format(employee_name=employee_name)
        db_cursor.execute(sql_query)
        row_data = db_cursor.fetchone()
        print('Employee Name    = ', str(row_data[0]).title())
        print('Employee Address = ', str(row_data[1]).title())
        print('Employee Age     = ', row_data[2])
        print('Employee Salary  = ', row_data[3])

        db_cursor.close()
        conn.close()

        return row_data

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
