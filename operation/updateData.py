import os
import sys
import psycopg2

from dotenv import load_dotenv, find_dotenv

from statement.sqlStatement import getSqlStatement as get_sql_statement
from operation.selectData import select_by_name
from beauti.updateDataBeautify import beautifyMenu as beautifiy_menu


def connect():
    conn = psycopg2.connect(host="localhost", database=os.getenv("DBNAME"),
                            user=os.getenv("USERNAME"), password="")
    return conn


def get_name_statement(name_searched):
    sql_statement = "SELECT id FROM company WHERE name='{name_searched}';"
    sql_query = sql_statement.format(name_searched=name_searched)
    return sql_query


def get_id_from_name(name_searched):
    conn = connect()
    db_cursor = conn.cursor()

    sql_statement = get_name_statement(name_searched)
    # print(sql_statement)

    db_cursor.execute(sql_statement)

    sql_query = db_cursor.fetchone()

    if sql_query is not None:
        return(str(sql_query[0]))
    else:
        return None
    db_cursor.close()
    conn.close()


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
    name_searched = str(input('enter employee name = '))

    id_name = get_id_from_name(name_searched)

    if id_name is not None:
        print('\n')
        notif = "\t{name_searched} are avaible in database !!!\t"
        found_notify = notif.format(name_searched=name_searched)
        print(found_notify)
        print('\n')

        print("\t UPDATE DATABASE \t\n")
        print("Current Data : ")
        select_by_name(name_searched)
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
        notif = "{name_searched} not avaible in our database"
        notif1 = notif.format(name_searched=name_searched)
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
