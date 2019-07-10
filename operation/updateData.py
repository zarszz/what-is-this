import psycopg2
import sys
from dotenv import load_dotenv, find_dotenv
import os

from statement.sqlStatement import getSqlStatement
from beauti.updateDataBeautify import beautifyMenu

def connect():
    conn = psycopg2.connect(host="localhost", database=os.getenv("DBNAME"),
                            user=os.getenv("USERNAME"), password="")
    return conn

# dbCursor = conn.cursor()


def getNameSqlStatement(namaYangDicari):
    sqlSearchStatement = "SELECT id FROM company WHERE name='{namaYangDicari}';"
    sqlStatement = sqlSearchStatement.format(namaYangDicari=namaYangDicari)
    return sqlStatement

def getIdName(namaYangDicari):
    conn = connect()
    dbCursor = conn.cursor()

    sqlSearchStatement = getNameSqlStatement(namaYangDicari)
    
    # print(sqlSearchStatement)

    dbCursor.execute(sqlSearchStatement)

    sqlSearchQuery = dbCursor.fetchone()

    if(sqlSearchQuery is not None):
        return(str(sqlSearchQuery[0]))
    else:
        return None

def mainUpdateDataFromDB(choice, idName):

    if(choice == '1'):
        sqlQuery = getSqlStatement('name', idName)
    elif(choice == '2'):
        sqlQuery = getSqlStatement('age', idName)
    elif(choice == '3'):
        sqlQuery = getSqlStatement('address', idName)
    elif(choice == '4'):
        sqlQuery = getSqlStatement('salary', idName)
    else:
        print("you entered wrong choice boss :v...")

    #  TODO passing Query to DATABASE
    # print('berhasil')
    # print('sqlquery = ', sqlQuery)
    try:
        conn = connect()
        dbCursor = conn.cursor()
        dbCursor.execute(sqlQuery)

        conn.commit()
        dbCursor.close()
    except (Exception, psycopg2.Error) as error:
        print("OPERATION FAILED ..........")
        print(error)
    except (Exception, psycopg2.DatabaseError) as error:
        print("OPERATION FAILED ..........")
        print(error)
    except (Exception, psycopg2.DataError) as error:
        print("OPERATION FAILED ..........")
        print(error)
    finally:
        print('\nOPEARTION SUCESSFULLY ......')

def mainMenu():

    os.system("clear")
    print(beautifyMenu())
    # print('\n')
    searchedName = str(input('enter employee name = '))

    idName = getIdName(searchedName)
    #print(idName)

    if(idName != None):
        #print(idName)
        print('\n')
        notif = "\t{searchedName} are avaible in database !!!\t"
        foundNotify = notif.format(searchedName=searchedName)
        print(foundNotify)
        print('\n')
        print("\t UPDATE DATABASE \t")
        print("Select data will be updated : ")
        print("1. Employee Name")
        print("2. Employee Age")
        print("3. Employee Address")
        print("4. Employee Salary")
        print('\n')
        updateChoice = str(input("Enter Your Choice ->  "))
        mainUpdateDataFromDB(updateChoice, idName)
        print('\n')
    elif idName == None:
        notif = "{searchedName} not avaible in our database"
        notif1 = notif.format(searchedName=searchedName)
        print(notif1)

def updateDataMain():
    trying = 'te'
    while trying != 'n':
        mainMenu()
        print('\n')
        print('enter (y) to update data again and (n) to close this menu')
        print('\n')
        print('update data again ?? (y/n) -> ', end='')
        trying = str(input())
        os.system('clear')

