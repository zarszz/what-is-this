import psycopg2
import sys
from dotenv import load_dotenv, find_dotenv
import os

def connect():
    conn = psycopg2.connect(host="localhost", database=os.getenv("DBNAME"),
                            user=os.getenv("USERNAME"), password="")
    return conn

# dbCursor = conn.cursor()


def getNameSqlStatement(namaYangDicari):
    sqlSearchStatement = "SELECT id FROM company WHERE name='{namaYangDicari}';".format(
        namaYangDicari=namaYangDicari)
    return sqlSearchStatement


def getAlamatStatement(pilihan, userId):

    updateData = str(input('masukkan alamat yang baru : '))

    sqlStatement1 = "UPDATE company SET address='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        pilihan=pilihan, updateData=updateData, userId=userId)

    return sqlStatement


def getNamaStatement(pilihan, userId):

    updateData = str(input('masukkan nama yang baru : '))

    sqlStatement1 = "UPDATE company SET name='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        pilihan=pilihan, updateData=updateData, userId=userId)

    return sqlStatement


def getUmurStatement(pilihan, userId):
    updateData = int(input('masukkan umur yang baru : '))

    sqlStatement1 = "UPDATE company SET age='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        pilihan=pilihan, updateData=updateData, userId=userId)

    return sqlStatement


def getGajiStatement(pilihan, userId):
    updateData = float(input('masukkan gaji yang baru : '))

    sqlStatement1 = "UPDATE company SET salary='{updateData}' WHERE id={userId};"

    sqlStatement = sqlStatement1.format(
        pilihan=pilihan, updateData=updateData, userId=userId)

    return sqlStatement


def getSqlStatement(pilihan, userId):

    if(pilihan == 'alamat'):
        sqlStatement = getAlamatStatement(pilihan, userId)
        return sqlStatement
    if(pilihan == 'umur'):
        sqlStatement = getUmurStatement(pilihan, userId)
        return sqlStatement
    if(pilihan == 'nama'):
        sqlStatement = getNamaStatement(pilihan, userId)
        return sqlStatement
    if(pilihan == 'gaji'):
       sqlStatement = getGajiStatement(pilihan, userId)
       return sqlStatement


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