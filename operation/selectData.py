import os 
import psycopg2

from operation.connector import conn as connector
from operation.specific_select import *

def selectFromDB():
    '''
    '''
    try:
        conn = connector()
        dbCursor = conn.cursor()

        dbCursor.execute("SELECT name,age,address,salary FROM company")
        print("The number of row = ", dbCursor.rowcount)
        row = dbCursor.fetchone()

        while row is not None:
            print(row)
            row = dbCursor.fetchone()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print("fetch sucess.........")     

def specific_select(choice):
    '''
    '''
    if(choice == '1'):
        selectFromDB()
    elif(choice == '2'):
        select_specific_by_data('address')
    elif(choice == '3'):
        select_specific_by_data('age')

def select_data_menu():
    '''
    '''
    os.system('clear')
    print('\tSELECT DATA MENU\t')
    print('Please Choose Option Below')
    print('1. Select All Data')
    print('2. Select Employee Address')
    print('3. Select Employee Age')
    choice = str(input('Enter Your Choice -> '))
    specific_select(choice)

def selectByName(employeeName):
    '''
    '''
    try:
        conn = connector()
        dbCursor = conn.cursor()

        statement = "SELECT name,address,age FROM company WHERE name='{employeeName}';"
        sqlQuery = statement.format(employeeName=employeeName)

        dbCursor.execute(sqlQuery)
        rowData = dbCursor.fetchone()
        print('Employee Name    = ', str(rowData[0]).capitalize())
        print('Employee Address = ', rowData[1])
        print('Employee Age     = ', rowData[2])
        
        return rowData

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
