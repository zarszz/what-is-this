import os
import sys

from operation.connector import conn as connect
from statement.sqlStatement import getSqlStatement as get_sql_statement
from operation.selectData import select_by_name, select_id_by_name
from beauti.updateDataBeautify import beautifyMenu as beautifiy_menu


def main_update_from_db(choice, id_name):
    print('\n')
    if choice is '1':
        sql_query = get_sql_statement('name', id_name)
    elif choice is '2':
        sql_query = get_sql_statement('age', id_name)
    elif choice is '3':
        sql_query = get_sql_statement('address', id_name)
    elif choice is '4':
        sql_query = get_sql_statement('salary', id_name)
    else:
        print("you entered wrong choice boss :v...")

    if choice in ('1', '2', '3', '4'):
        try:
            conn = connect()
            db_cursor = conn.cursor()
            db_cursor.execute(sql_query)

            conn.commit()
            db_cursor.close()
        except (Exception, psycopg2.Error) as error:
            print("OPERATION FAILED ..........")
            print(error)
        except (Exception, psycopg2.DatabaseError) as error:
            print("OPERATION FAILED ..........")
            print(error)
        except (Exception, psycopg2.DataError) as error:
            print("OPERATION FAILED ..........")
            print(error)
    else:
        print('\nPlease Enter Valid Choice(1/2/3/4) !!!!')


def main_menu():

    os.system("clear")
    print(beautifiy_menu())
    employee_name = str(input('enter employee name = '))

    id_name = select_id_by_name(employee_name)

    if id_name is not None:
        print('\n')
        notif = "\t{employee_name} are avaible in database !!!\t"
        found_notify = notif.format(employee_name=employee_name)
        print(found_notify)
        print('\n')

        print("\t UPDATE DATABASE \t\n")
        print("Current Data : ")
        select_by_name(employee_name)
        print('\n')

        print("Select data will be updated : ")
        print("1. Employee Name")
        print("2. Employee Age")
        print("3. Employee Address")
        print("4. Employee Salary")
        update_choice = str(input("Enter Your Choice ->  "))
        main_update_from_db(update_choice, id_name)

        print('\n')
    elif id_name is None:
        notif = "{employee_name} not avaible in our database"
        notif1 = notif.format(employee_name=employee_name)
        print(notif1)


def update_data_main():
    trying = 'te'
    while trying != 'n':
        main_menu()
        print('enter (y) to update data again and (n) to close this menu')
        print('\n')
        print('update data again ?? (y/n) -> ', end='')
        trying = str(input())
        os.system('clear')
