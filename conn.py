'''
'   Main Program
'''
import sys
import os
import psycopg2

from dotenv import load_dotenv

from operation.updateData import update_data_main
from operation.connector import conn as connector
from operation.connector import testconnector
from operation.createData import create_data_to_db
from operation.selectData import select_data_menu
from operation.deleteData import delete_data_main

load_dotenv(verbose=True)


def get_row_number():
    """
    "   Get sum of row number in table
    "   return integer()
    "
    """
    conn = psycopg2.connect(host="localhost", database=os.getenv('DBNAME'),
                            user=os.getenv('USERNAME'), password='')
    db_cursor = conn.cursor()
    db_cursor.execute("SELECT * FROM company")
    return int(db_cursor.rowcount)

def main():
    """
        Main program
    """
    os.system('clear')
    print("\t\t->> \t DB CONNECTOR  \t <<-\t\t")
    print("\t\t     Created by z@rszz<> \t\t \n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@                                 @@")
    print("@@      DATABASE MANAGEMENT        @@")
    print("@@                                 @@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Main Menu")
    print("1. Test Connection")
    print("2. Fetch Data")
    print("3. Insert Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit Program")
    print("choice -> ", end='')
    menu_choice = str(input())
    if menu_choice == "1":
        testconnector()
    elif menu_choice == "2":
        select_data_menu()
    elif menu_choice == "3":
        rownumber = get_row_number()
        create_data_to_db(rownumber)
    elif menu_choice == "4":
        update_data_main()
    elif menu_choice == "5":
        delete_data_main()
    elif menu_choice == "6":
        sys.exit()
    else:
        print("Error choice. . .")
        sys.exit()


if __name__ == "__main__":
    decision = "absolutelyalwaysfalse"
    while decision not in ('n', 'N'):
        main()
        decision = str(input("Wanna try again ?? (y/n) -> "))
