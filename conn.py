import psycopg2
import sys
from dotenv import load_dotenv, find_dotenv
import os

from updateData import updateDataMain

load_dotenv(verbose=True)

def connect():
    try:
        print('Connecting to PostgreSQL database . . . .')
        conn = psycopg2.connect(host="localhost", database=os.getenv('DBNAME'),
                                user=os.getenv('USERNAME'), password="")
        if(conn is not None):
            print("Database Connected....")
            return conn
        else:
            print("Database Error")

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version : ')
        cur.execute('SELECT version()')

        # display the postgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close communication to postgreSQL
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


def getRowNumber():
    conn = connect()
    dbCursor = conn.cursor()
    dbCursor.execute("SELECT * FROM company")
    x = dbCursor.rowcount
    return int(x)


def createDataToDB():
    pegawai_id = None
    try:
        conn = connect()
        dbCursor = conn.cursor()
        namaPegawai = str(input("masukkan nama pegawai : "))
        umurPegawai = str(input("masukkan umur pegawai : "))
        alamatPegawai = str(input("masukkan alamat gepawai : "))
        gajiPegawai = float(input("masukkan gaji peagawi :"))
        pegawai_db_id = getRowNumber() + 1

        sql = "INSERT INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES({pegawai_db_id}, '{namaPegawai}', {umurPegawai}, '{alamatPegawai}', {gajiPegawai}) RETURNING id;"
        sqlQuery = sql.format(pegawai_db_id=str(pegawai_db_id), namaPegawai=namaPegawai,
                              umurPegawai=umurPegawai, alamatPegawai=alamatPegawai, gajiPegawai=str(gajiPegawai))

        dbCursor.execute(sqlQuery)
        conn.commit()
        dbCursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()
        print("INSERT DATA SUKSES ......")


def selectFromDB():
    try:
        conn = connect()
        dbCursor = conn.cursor()

        dbCursor.execute("SELECT * FROM company")
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

def main():
    os.system('clear')
    print("\t\t->> \t DB CONNECTOR  \t <<-\t\t\n\n")
    print("\t\t     created by z@rszz<> \t\t \n\n")
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
        connect()
    elif(menuPilihan == "2"):
        selectFromDB()
    elif(menuPilihan == "3"):
        createDataToDB()
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
