import psycopg2
import sys
import os

from dotenv import load_dotenv

from operation.updateData import updateDataMain
from operation.connector import conn as connector
from operation.createData import createDataToDB
from operation.selectData import selectFromDB

load_dotenv(verbose=True)


def getRowNumber():
    conn = psycopg2.connect(host="localhost", database=os.getenv('DBNAME'),
                              user=os.getenv('USERNAME'), password='')
    dbCursor = conn.cursor()
    dbCursor.execute("SELECT * FROM company")
    x = dbCursor.rowcount
    return int(x)

def main():
    os.system('clear')
    print("\t\t->> \t DB CONNECTOR  \t <<-\t\t")
    print("\t\t     created by z@rszz<> \t\t \n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@                                 @@")
    print("@@      DATABASE MANAGEMENT        @@")
    print("@@                                 @@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")    
    print("pilihan menu")
    print("1. test connection")
    print("2. fetch data")
    print("3. insert data")
    print("4. update data")
    print("pilihan ->", end='')
    menuPilihan = str(input())
    if(menuPilihan == "1"):
        connector()
    elif(menuPilihan == "2"):
        selectFromDB()
    elif(menuPilihan == "3"):
        rownumber = getRowNumber()
        createDataToDB(rownumber)
    elif(menuPilihan == "4"):
        updateDataMain()
    else:
        print("Pilihan error . . .")
        sys.exit()


if __name__ == "__main__":
    nyoba = "te"
    while (nyoba != 'n') and (nyoba != 'N'):
        main()
        nyoba = str(input("Mau nyoba lagi ?? (y/n)"))
