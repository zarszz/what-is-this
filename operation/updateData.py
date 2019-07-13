import os
import sys
import psycopg2

from dotenv import load_dotenv, find_dotenv

from statement.sqlStatement import getSqlStatement as get_sql_statement
from beauti.updateDataBeautify import beautifyMenu


def connect():
    conn = psycopg2.connect(host="localhost", database=os.getenv("DBNAME"),
                            user=os.getenv("USERNAME"), password="")
    return conn

# db_cursor = conn.cursor()


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


def main_update_from_db(choice, idName):
    print('\n')
    if choice is '1':
        sql_query = get_sql_statement('name', idName)
    elif choice is '2':
        sql_query = get_sql_statement('age', idName)
    elif choice is '3':
        sql_query = get_sql_statement('address', idName)
    elif choice is '4':
        sql_query = get_sql_statement('salary', idName)
    else:
        print("you entered wrong choice boss :v...")

    #  TODO passing Query to DATABASE
    # print('berhasil')
    # print('sql_query = ', sql_query)
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
    print(beautifyMenu())
    # print('\n')
    name_searched = str(input('enter employee name = '))

    idName = get_id_from_name(name_searched)
    # print(idName)

    if idName is not None:
        # print(idName)
        print('\n')
        notif = "\t{name_searched} are avaible in database !!!\t"
        foundNotify = notif.format(name_searched=name_searched)
        print(foundNotify)
        print('\n')
        print("\t UPDATE DATABASE \t\n")
        print("Select data will be updated : ")
        print("1. Employee Name")
        print("2. Employee Age")
        print("3. Employee Address")
        print("4. Employee Salary")
        updateChoice = str(input("Enter Your Choice ->  "))
        main_update_from_db(updateChoice, idName)
        print('\n')
    elif idName is None:
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