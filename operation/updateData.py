import psycopg2
import sys
from dotenv import load_dotenv, find_dotenv
import os

from statement.sqlStatement import getSqlStatement

def connect():
    conn = psycopg2.connect(host="localhost", database=os.getenv("DBNAME"),
                            user=os.getenv("USERNAME"), password="")
    return conn

# dbCursor = conn.cursor()


def getNameSqlStatement(namaYangDicari):
    sqlSearchStatement = "SELECT id FROM company WHERE name='{namaYangDicari}';".format(
        namaYangDicari=namaYangDicari)
    return sqlSearchStatement

def getIdNama(namaYangDicari):
    conn = connect()
    dbCursor = conn.cursor()

    sqlSearchStatement = getNameSqlStatement(namaYangDicari=namaYangDicari)
    
    #print(sqlSearchStatement)

    dbCursor.execute(sqlSearchStatement)

    sqlSearchQuery = dbCursor.fetchone()

    if(sqlSearchQuery is not None):
        return(str(sqlSearchQuery[0]))
    else:
        return None

def mainUpdateDataFromDB(pilihan, idNama):

    if(pilihan == '1'):
        sqlQuery = getSqlStatement('nama', idNama)
    elif(pilihan == '2'):
        sqlQuery = getSqlStatement('umur', idNama)
    elif(pilihan == '3'):
        sqlQuery = getSqlStatement('alamat', idNama)
    elif(pilihan == '4'):
        sqlQuery = getSqlStatement('gaji', idNama)
    else:
        print("salah pilihan boss :v...")

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
        print("OPERASI GAGAL ..........")
        print(error)
    except (Exception, psycopg2.DatabaseError) as error:
        print("OPERASI GAGAL ..........")
        print(error)
    except (Exception, psycopg2.DataError) as error:
        print("OPERASI GAGAL ..........")
        print(error)
    finally:
        print('\nOPERASI BERHASIL ......')

def beautifyMenu():
    beauti = """
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            @@                               @@
            @@          UPDATE DATA          @@
            @@                               @@
            @@                               @@
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
             """
    return beauti


def mainMenu():

    os.system("clear")
    print(beautifyMenu())
    # print('\n')
    namaYangDicari = str(input('masukkan nama yang akan dicari = '))

    idName = getIdNama(namaYangDicari)

    if(idName != None):
        # print(idName)
        print('\n')
        notif = "\t{namaYangDicari} terdapat dalam database !!!\t"
        notifKetemu = notif.format(namaYangDicari=namaYangDicari)
        print(notifKetemu)
        print('\n')
        print("\t UPDATE DATABASE \t")
        print("Pilih data yang akan diupdate ")
        print("1. Nama")
        print("2. umur")
        print("3. alamat")
        print("4. gaji")
        print('\n')
        updateChoice = str(input("masukkan pilihan -> "))
        mainUpdateDataFromDB(updateChoice, idName)
    elif idName == None:
        notif = "{namaYangDicari} tidak terdapat pada data"
        notif1 = notif.format(namaYangDicari=namaYangDicari)
        print(notif1)

def updateDataMain():
    nyoba = 'te'
    while nyoba != 'n':
        mainMenu()
        print('\n')
        print('apabila mau update data atau nyoba lagi silahkan ketik (y)')
        print('\n')
        print('ulangi lagi ?? (y/n) ->', end='')
        nyoba = str(input())