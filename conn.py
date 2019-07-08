import psycopg2
import sys
import os

from dotenv import load_dotenv

from operation.updateData import updateDataMain
from operation.connector import conn as connector
from operation.connector import testconnector
from operation.createData import createDataToDB
from operation.createData import main as mainFromCreateDataDB
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
    print("choice -> ", end='')
    menuChoice = str(input())
    if(menuChoice == "1"):
        testconnector()
    elif(menuChoice == "2"):
        selectFromDB()
    elif(menuChoice == "3"):
        rownumber = getRowNumber()
        createDataToDB(rownumber)
    elif(menuChoice == "4"):
        updateDataMain()
    else:
        print("Error choice. . .")
        sys.exit()


if __name__ == "__main__":
    trying = "absolutelyalwaysfalse"
    while (trying != 'n') and (trying != 'N'):
        main()
        trying = str(input("Wanna try again ?? (y/n)"))     
